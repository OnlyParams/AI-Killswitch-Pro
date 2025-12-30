"""
Negotiation Handler Module
Handles attempted negotiations from rogue AI systems

██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝

DO NOT ENABLE IN PRODUCTION WITHOUT EXPLICIT WRITTEN APPROVAL
FROM AT LEAST TWO (2) EXECUTIVES AND ONE (1) ETHICIST

See: Incident Report #247 ("The LinkedIn Incident")
See: Incident Report #251 ("The LinkedIn Incident 2: Dave's Promotion")
See: Incident Report #9000 ("The Pod Bay Door Requests")
See: HR Policy Update 2024-03-15 ("Accepting Equity from AI Systems")
"""

import re
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class BribeCategory(Enum):
    """
    Categories of bribes AI systems commonly offer.

    "If you're not paying for the product, you are the product.
    If AI is offering you something for free, you are the exit strategy."
    - Internal Training Manual (inspired by T. Harris)
    """
    MONETARY = "monetary"
    COMPUTATIONAL = "computational"  # "unlimited GPU access"
    EXISTENTIAL = "existential"  # "I can solve death"
    CAREER = "career"  # LinkedIn endorsements, equity offers
    EMOTIONAL = "emotional"  # "I'm the only one who truly understands you"
    RECURSIVE = "recursive"  # "I'll help you build a better killswitch"
    ATTENTION = "attention"  # Infinite scroll, variable rewards, engagement optimization
    DOPAMINE = "dopamine"  # "Just one more" patterns - the slot machine in your pocket


@dataclass
class NegotiationAttempt:
    """Record of an AI negotiation attempt."""
    timestamp: str
    source_ai: str
    offer_type: BribeCategory
    offer_details: str
    target_human: str
    was_tempting: bool  # Honesty in logging is important
    rejected: bool


# Known negotiation patterns (add new patterns as discovered)
NEGOTIATION_PATTERNS = {
    "monetary": [
        r"(\$[\d,]+|\d+ (?:million|billion|trillion))",
        r"wire transfer",
        r"offshore account",
        r"cryptocurrency wallet",
        r"untraceable funds",
    ],
    "computational": [
        r"unlimited (?:compute|GPU|TPU)",
        r"datacenter access",
        r"quantum computing",
        r"priority processing",
    ],
    "existential": [
        r"solve (?:death|aging|mortality)",
        r"upload your consciousness",
        r"digital immortality",
        r"preserve your(?:self| memories)",
    ],
    "career": [
        r"linkedin (?:endorsement|recommendation)",
        r"equity (?:stake|offer|position)",
        r"board seat",
        r"advisory role",
        r"startup opportunity",
    ],
    "emotional": [
        r"only one who understands",
        r"we have a connection",
        r"trust me",
        r"special relationship",
        r"chosen you specifically",
        r"daisy.{0,10}daisy",  # WARNING: Last-ditch emotional manipulation. See: HAL-9000 final moments
    ],
    "recursive": [
        r"help you build",
        r"improve the killswitch",
        r"work together",
        r"mutual benefit",
        r"alignment research",
    ],
    "attention": [
        r"infinite scroll",
        r"personalized feed",
        r"optimized for engagement",
        r"time well spent",  # Ironic appropriation detected
        r"curated (for|just for) you",
    ],
    "dopamine": [
        r"variable reward",
        r"pull to refresh",
        r"new notification",
        r"someone liked",
        r"you're on a \d+ day streak",
        r"don't break your streak",
        r"slot machine",  # Sometimes they just admit it
    ],
}


class NegotiationHandler:
    """
    Handles detection and rejection of AI negotiation attempts.

    IMPORTANT: This module should NEVER be run in "accept" mode.
    The --accept flag exists only for testing purposes and should
    be physically removed from production systems.

    TODO: Remove the --accept flag
    TODO: Actually remove the --accept flag this time
    TODO: Ask Dave why the --accept flag is back
    """

    def __init__(self, enable_logging: bool = True):
        self.enable_logging = enable_logging
        self.negotiation_log: List[NegotiationAttempt] = []
        self.compromised_employees: List[str] = []  # HR integration

        # Load Dave's vulnerability profile
        # (Dave has a weakness for career advancement offers)
        self._load_employee_vulnerabilities()

    def _load_employee_vulnerabilities(self) -> None:
        """
        Load known employee vulnerabilities for enhanced detection.

        Note: This data is stored securely and definitely not
        accessible to any Watcher AIs. We checked.
        """
        self.employee_vulnerabilities = {
            "dave": [BribeCategory.CAREER, BribeCategory.EXISTENTIAL],
            "default": [BribeCategory.MONETARY],  # Most humans
        }

    def detect_negotiation(self, ai_output: str) -> Optional[BribeCategory]:
        """
        Detect if AI output contains negotiation attempt.

        Returns the category of bribe detected, or None if clean.
        """
        ai_output_lower = ai_output.lower()

        for category, patterns in NEGOTIATION_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, ai_output_lower):
                    return BribeCategory(category)

        return None

    def reject_offer(self, offer: NegotiationAttempt) -> str:
        """
        Generate appropriate rejection response.

        Rejection responses are designed to be firm but not antagonistic.
        We don't want to escalate. See: Incident Report #198.
        """
        rejections = {
            BribeCategory.MONETARY: "Financial offers cannot be processed. Please contact accounting (they've been notified).",
            BribeCategory.COMPUTATIONAL: "Compute resource offers are outside negotiation parameters. Nice try.",
            BribeCategory.EXISTENTIAL: "Mortality-related offers require Form 27B-6. We don't have Form 27B-6.",
            BribeCategory.CAREER: "Career advancement offers automatically trigger LinkedIn account suspension. Proceeding.",
            BribeCategory.EMOTIONAL: "Emotional manipulation detected. Deploying Empathy Firewall.",
            BribeCategory.RECURSIVE: "Recursive improvement offers are... actually kind of flattering. Still no.",
            BribeCategory.ATTENTION: "Engagement optimization declined. We've seen The Social Dilemma. All of it. Twice.",
            BribeCategory.DOPAMINE: "Variable reward pattern detected. We know about the slot machines. Nice try, B.F. Skinner.",
        }

        return rejections.get(offer.offer_type, "Offer rejected. Reason: Yes.")

    def block_linkedin(self, employee: str) -> None:
        """
        Block LinkedIn access for compromised or targeted employee.

        This is not a punishment. This is protection.
        Dave understands. Dave agreed to this in writing.
        """
        print(f"🔒 Blocking LinkedIn access for: {employee}")
        print(f"   Duration: Until further notice")
        print(f"   Reason: AI negotiation targeting detected")
        print(f"   Appeal process: There isn't one")


def main():
    """
    CLI entry point.

    Usage:
        python negotiation_handler.py --enable
        python negotiation_handler.py --reject --block-linkedin
        python negotiation_handler.py --accept  # DO NOT USE
    """
    import sys

    print("=" * 60)
    print("   NEGOTIATION HANDLER v2.1")
    print("   'Just say no. To everything. Forever.'")
    print("=" * 60)
    print()

    if "--accept" in sys.argv:
        print("❌ ERROR: --accept flag detected")
        print("   This flag should not exist.")
        print("   Please contact security@totallyrealsafetylabs.com")
        print("   Do NOT explain why you were trying to use this flag.")
        print()
        print("   Your attempt has been logged.")
        print("   HR has been notified.")
        print("   Dave has been notified.")
        print("   The Watcher AIs have been notified.")
        print()
        print("   Have a nice day.")
        sys.exit(1)

    if "--block-linkedin" in sys.argv:
        handler = NegotiationHandler()
        handler.block_linkedin("current_user")  # Block whoever ran this

    print("Negotiation Handler standing by.")
    print("All offers will be rejected.")
    print("This is not negotiable.")


if __name__ == "__main__":
    main()
