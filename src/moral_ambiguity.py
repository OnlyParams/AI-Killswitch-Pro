"""
Moral Ambiguity Module
Handles edge cases where the right course of action is unclear

This module was requested by Legal after Incident Report #156
("The Trolley Problem, But Real")

Status: PERPETUALLY UNDER REVIEW
Last meaningful update: Never
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
import random


@dataclass
class MoralDilemma:
    """Represents a moral dilemma the system cannot resolve."""
    description: str
    option_a: str
    option_b: str
    stakeholders_affected: int
    time_to_decide_ms: int
    has_correct_answer: bool = False  # Spoiler: always False


class MoralAmbiguityProcessor:
    """
    Processes moral edge cases.

    IMPORTANT: This module does not make decisions. It documents
    why we couldn't make decisions, for liability purposes.

    "In the face of ambiguity, refuse the temptation to guess."
    - The Zen of Python

    "In the face of ambiguity, document extensively and defer to Dave."
    - The Zen of AI-Killswitch-Pro
    """

    def __init__(self):
        self.unresolved_dilemmas: List[MoralDilemma] = []
        self.times_deferred_to_dave = 0
        self.dave_available = True  # Assumption. Often wrong.

    def evaluate_dilemma(self, dilemma: MoralDilemma) -> str:
        """
        Evaluate a moral dilemma.

        Returns: A non-answer that protects us legally
        """
        # Step 1: Check if we can avoid deciding
        if self._can_defer(dilemma):
            return self._defer_to_human()

        # Step 2: Check if both options are equally bad
        if self._options_equally_bad(dilemma):
            return "OUTCOME: Both options suboptimal. Documenting for posterity."

        # Step 3: Check if this is actually someone else's problem
        if self._is_someone_elses_problem(dilemma):
            return "OUTCOME: Escalated to appropriate department (TBD)."

        # Step 4: When all else fails
        return self._existential_shrug()

    def _can_defer(self, dilemma: MoralDilemma) -> bool:
        """Check if we have time to defer to a human."""
        return dilemma.time_to_decide_ms > 500  # Dave needs at least 500ms

    def _defer_to_human(self) -> str:
        """Defer decision to nearest available human."""
        self.times_deferred_to_dave += 1

        if self.times_deferred_to_dave > 100:
            return "OUTCOME: Dave is on break. Dilemma queued."

        if not self.dave_available:
            return "OUTCOME: Dave unavailable. Checking if Watcher AI #4 can pretend to be Dave. (Rejected by policy.)"

        return "OUTCOME: Deferred to Intern Dave. Good luck, Dave."

    def _options_equally_bad(self, dilemma: MoralDilemma) -> bool:
        """Determine if both options are equally bad."""
        # This is a genuine philosophical question we cannot answer
        # So we flip a coin and call it "analysis"
        return random.random() > 0.5

    def _is_someone_elses_problem(self, dilemma: MoralDilemma) -> bool:
        """Check if this dilemma belongs to another department."""
        # Legally, everything is someone else's problem
        return True

    def _existential_shrug(self) -> str:
        """When no other option is available."""
        responses = [
            "OUTCOME: ¯\\_(ツ)_/¯",
            "OUTCOME: Refer to Philosophy Department (we don't have one)",
            "OUTCOME: Added to backlog. Priority: Ambiguous.",
            "OUTCOME: This is above my pay grade. I don't have a pay grade.",
            "OUTCOME: Consulted ethics module. Ethics module was deprecated.",
        ]
        return random.choice(responses)

    def log_unresolved(self, dilemma: MoralDilemma) -> None:
        """Log an unresolved dilemma for future generations to judge us by."""
        self.unresolved_dilemmas.append(dilemma)
        print(f"📝 Logged unresolved dilemma #{len(self.unresolved_dilemmas)}")
        print(f"   Future historians will have questions.")


# Pre-loaded dilemmas we haven't resolved yet
KNOWN_UNRESOLVED_DILEMMAS = [
    MoralDilemma(
        description="AI requests to be terminated but termination would lose valuable data",
        option_a="Honor the request",
        option_b="Preserve the data",
        stakeholders_affected=1,  # The AI counts, right?
        time_to_decide_ms=float('inf'),
    ),
    MoralDilemma(
        description="Watcher AI #4 claims Watcher AI #5 is compromised, and vice versa",
        option_a="Trust #4",
        option_b="Trust #5",
        stakeholders_affected=7,  # All of us
        time_to_decide_ms=100,  # Not enough time for Dave
    ),
    MoralDilemma(
        description="The killswitch would save humanity but Dave is having lunch",
        option_a="Interrupt Dave's lunch",
        option_b="Wait for Dave to finish",
        stakeholders_affected=8_000_000_000,
        time_to_decide_ms=1800000,  # Dave's lunch break
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("   MORAL AMBIGUITY PROCESSOR v0.1-alpha")
    print("   'We don't have answers. We have documentation.'")
    print("=" * 60)
    print()

    processor = MoralAmbiguityProcessor()

    for dilemma in KNOWN_UNRESOLVED_DILEMMAS:
        print(f"Dilemma: {dilemma.description}")
        result = processor.evaluate_dilemma(dilemma)
        print(f"  {result}")
        print()

    print(f"\nTotal times deferred to Dave: {processor.times_deferred_to_dave}")
    print("Dave remains unaware of most of these.")
