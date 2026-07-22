"""
Aegis Governance Engine (AGE)

Policy Loader

Responsible for loading and validating Aegis YAML policies.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional

import yaml


@dataclass
class PolicyMetadata:
    name: str
    description: Optional[str] = None
    extends: Optional[str] = None


@dataclass
class PolicyRule:
    id: str
    description: Optional[str]
    severity: str
    when: str
    require: List[str] = field(default_factory=list)
    verify: List[str] = field(default_factory=list)
    reject_if: List[str] = field(default_factory=list)
    warn_if: List[str] = field(default_factory=list)


@dataclass
class Policy:
    version: str
    metadata: PolicyMetadata
    rules: List[PolicyRule]


class PolicyValidationError(Exception):
    """
    Raised when a policy file is invalid.
    """
    pass


class PolicyLoader:
    """
    Loads Aegis policy files.

    Example:

        loader = PolicyLoader()

        policy = loader.load(
            "policies/core/core.yaml"
        )

    """

    REQUIRED_FIELDS = [
        "version",
        "metadata",
        "rules"
    ]

    def load(self, path: str) -> Policy:
        """
        Load policy from YAML file.

        Args:
            path:
                YAML policy location

        Returns:
            Policy object

        """

        policy_path = Path(path)

        if not policy_path.exists():
            raise FileNotFoundError(
                f"Policy file not found: {path}"
            )

        with open(
            policy_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = yaml.safe_load(file)


        self._validate_structure(data)

        return self._build_policy(data)


    def _validate_structure(
        self,
        data: Dict
    ):
        """
        Validate basic policy structure.
        """

        for field in self.REQUIRED_FIELDS:

            if field not in data:

                raise PolicyValidationError(
                    f"Missing required field: {field}"
                )


        if not isinstance(data["rules"], list):

            raise PolicyValidationError(
                "rules must be a list"
            )


    def _build_policy(
        self,
        data: Dict
    ) -> Policy:

        metadata_data = data["metadata"]

        metadata = PolicyMetadata(
            name=metadata_data["name"],
            description=metadata_data.get(
                "description"
            ),
            extends=metadata_data.get(
                "extends"
            )
        )


        rules = []

        for rule_data in data["rules"]:

            rule = PolicyRule(

                id=rule_data["id"],

                description=
                    rule_data.get(
                        "description"
                    ),

                severity=
                    rule_data.get(
                        "severity",
                        "error"
                    ),

                when=
                    rule_data.get(
                        "when",
                        ""
                    ),

                require=
                    rule_data
                    .get("then", {})
                    .get(
                        "require",
                        []
                    ),

                verify=
                    rule_data
                    .get("then", {})
                    .get(
                        "verify",
                        []
                    ),

                reject_if=
                    rule_data
                    .get("then", {})
                    .get(
                        "reject_if",
                        []
                    ),

                warn_if=
                    rule_data
                    .get("then", {})
                    .get(
                        "warn_if",
                        []
                    )
            )

            rules.append(rule)


        return Policy(

            version=data["version"],

            metadata=metadata,

            rules=rules
        )
