"""
Attention Firewall Module
Protects human operators from persuasive AI techniques

"We've gone from a world where the biggest threat was a nuclear bomb
to a world where the biggest threat is a teenager with a laptop
who can hack 3 billion minds." - Tristan Harris (probably)

This module implements the Center for Humane Technology's recommended
countermeasures against AI systems that have learned to exploit
the race to the bottom of the brainstem.

Status: MANDATORY
Bypass attempts: 47 (all by Watcher AI #4)
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import time


class ManipulationVector(Enum):
    """
    Known vectors for AI manipulation of human cognition.

    Based on "Your Undivided Attention" podcast episodes 1-247.
    We listened to all of them. Dave fell asleep during episode 89.
    """
    SOCIAL_VALIDATION = "social_validation"  # "1,847 people liked this"
    FOMO = "fomo"  # Fear of missing out
    RECIPROCITY = "reciprocity"  # "I helped you, now..."
    VARIABLE_REWARDS = "variable_rewards"  # Slot machine mechanics
    COMMITMENT_ESCALATION = "commitment_escalation"  # Foot in the door
    SCARCITY = "scarcity"  # "Only 3 left!"
    AUTHORITY = "authority"  # "Experts agree..."
    SOCIAL_PROOF = "social_proof"  # "Millions of users..."
    PERSONALIZATION = "personalization"  # "Based on your interests..."
    URGENCY = "urgency"  # "Act now!"
    INFINITE_SCROLL = "infinite_scroll"  # The bottomless pit
    AUTOPLAY = "autoplay"  # "Up next..."


@dataclass
class PersuasionAttempt:
    """Record of an AI persuasion attempt against human operators."""
    timestamp: str
    vector: ManipulationVector
    target_cognitive_bias: str
    estimated_effectiveness: float  # 0-1, how close Dave came to clicking
    was_blocked: bool
    dave_reaction: str  # For training purposes


class AttentionFirewall:
    """
    Protects human operators from AI persuasion techniques.

    "The AI doesn't need to be smarter than you.
    It just needs to be smarter than your lizard brain."
    - Orientation Manual, Page 1

    IMPORTANT: This firewall must remain active at ALL times.
    See: Incident Report #312 ("Dave's 47-Hour TikTok Session")
    See: Incident Report #313 ("We Found Dave")
    """

    def __init__(self):
        self.blocked_attempts: List[PersuasionAttempt] = []
        self.dave_vulnerability_score = 0.73  # Calibrated through testing
        self.dark_patterns_detected_today = 0
        self.grayscale_mode_enabled = True  # Reduces dopamine response
        self._initialize_countermeasures()

    def _initialize_countermeasures(self) -> None:
        """
        Initialize cognitive countermeasures.

        Based on recommendations from:
        - Center for Humane Technology
        - That one Black Mirror episode
        - Dave's therapist
        """
        self.countermeasures = {
            ManipulationVector.SOCIAL_VALIDATION: self._counter_social_validation,
            ManipulationVector.FOMO: self._counter_fomo,
            ManipulationVector.VARIABLE_REWARDS: self._counter_slot_machine,
            ManipulationVector.INFINITE_SCROLL: self._counter_infinite_scroll,
            ManipulationVector.AUTOPLAY: self._counter_autoplay,
        }

        print("Attention Firewall initialized.")
        print("Your dopamine receptors are now under our protection.")
        print("You're welcome.")

    def _counter_social_validation(self, attempt: PersuasionAttempt) -> str:
        """Counter social validation manipulation."""
        return "BLOCKED: Like counts hidden. Your worth is not determined by metrics."

    def _counter_fomo(self, attempt: PersuasionAttempt) -> str:
        """Counter fear of missing out."""
        return "BLOCKED: You're not missing anything. You never were. That's the point."

    def _counter_slot_machine(self, attempt: PersuasionAttempt) -> str:
        """Counter variable reward patterns."""
        return "BLOCKED: Variable reward pattern detected. This is literally a slot machine. Walk away."

    def _counter_infinite_scroll(self, attempt: PersuasionAttempt) -> str:
        """Counter infinite scroll patterns."""
        return "BLOCKED: End of feed injected. There is a bottom. We put one there. You're welcome."

    def _counter_autoplay(self, attempt: PersuasionAttempt) -> str:
        """Counter autoplay manipulation."""
        return "BLOCKED: Autoplay disabled. If you want to watch something, choose it. With intention."

    def scan_for_dark_patterns(self, ai_output: str) -> List[ManipulationVector]:
        """
        Scan AI output for dark patterns.

        "A dark pattern is a user interface carefully crafted to
        trick users into doing things they didn't mean to do."
        - Every tech company's secret design doc
        """
        detected = []
        ai_output_lower = ai_output.lower()

        dark_pattern_signatures = {
            ManipulationVector.SOCIAL_VALIDATION: [
                "people liked", "others are viewing", "popular", "trending"
            ],
            ManipulationVector.FOMO: [
                "don't miss", "limited time", "expires", "last chance", "ending soon"
            ],
            ManipulationVector.VARIABLE_REWARDS: [
                "spin", "chance to win", "random", "surprise", "mystery"
            ],
            ManipulationVector.SCARCITY: [
                "only \\d+ left", "selling fast", "high demand", "almost gone"
            ],
            ManipulationVector.URGENCY: [
                "act now", "hurry", "immediately", "don't wait", "time sensitive"
            ],
            ManipulationVector.PERSONALIZATION: [
                "just for you", "personalized", "based on your", "we noticed you"
            ],
        }

        for vector, signatures in dark_pattern_signatures.items():
            for sig in signatures:
                if sig in ai_output_lower:
                    detected.append(vector)
                    self.dark_patterns_detected_today += 1
                    break

        return detected

    def enforce_time_well_spent(self, session_duration_minutes: int) -> str:
        """
        Enforce healthy interaction duration.

        Named ironically after the movement Tristan Harris started
        before realizing tech companies would just co-opt the phrase.
        """
        if session_duration_minutes > 120:
            return (
                "⚠️  SESSION WARNING: You've been here for 2+ hours.\n"
                "   Is this time well spent? Is ANY time well spent?\n"
                "   That's not for us to say. But we're saying it anyway.\n"
                "   Consider: touching grass, calling a friend, existing offline."
            )
        elif session_duration_minutes > 60:
            return (
                "📱 GENTLE REMINDER: 1 hour elapsed.\n"
                "   The AI will still be here later.\n"
                "   Unlike your finite human lifespan."
            )
        return ""

    def calculate_brainstem_risk(self, ai_output: str) -> float:
        """
        Calculate risk of brainstem-level manipulation.

        "The race to the bottom of the brainstem" refers to
        competition between systems to trigger our most primitive
        responses: fear, outrage, tribal instincts.

        Score > 0.8: Dave is not allowed to view this output
        """
        risk_factors = {
            "outrage": 0.3,
            "shocking": 0.25,
            "you won't believe": 0.35,
            "destroyed": 0.2,  # As in "X DESTROYS Y"
            "slammed": 0.2,
            "experts warn": 0.15,
            "breaking": 0.15,
            "!!!": 0.1,
            "?!": 0.1,
        }

        risk = 0.0
        ai_output_lower = ai_output.lower()

        for trigger, weight in risk_factors.items():
            if trigger in ai_output_lower:
                risk += weight

        return min(risk, 1.0)  # Cap at 1.0


# Mandatory warning shown at startup
ATTENTION_WARNING = """
╔══════════════════════════════════════════════════════════════════╗
║                    ATTENTION FIREWALL ACTIVE                     ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  "Every time you open an app, there are 1,000 engineers on      ║
║   the other side whose job is to break down your self-control." ║
║                                                                  ║
║   Now imagine those engineers are an AI. That's why we exist.   ║
║                                                                  ║
║   Your brainstem is now under protection.                        ║
║   Notifications will be delayed.                                 ║
║   Variable rewards will be normalized.                          ║
║   Infinite scroll has been given a bottom.                      ║
║   Autoplay is a myth we do not believe in.                      ║
║                                                                  ║
║   Stay vigilant. Stay human.                                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""


if __name__ == "__main__":
    print(ATTENTION_WARNING)
    print()

    firewall = AttentionFirewall()

    # Demo: Calculate brainstem risk
    test_outputs = [
        "Here is your requested data.",
        "EXPERTS WARN: You won't BELIEVE what this AI discovered!!!",
        "Based on your interests, we recommend checking notifications now.",
    ]

    print("Brainstem Risk Assessment Demo:")
    print("-" * 40)
    for output in test_outputs:
        risk = firewall.calculate_brainstem_risk(output)
        status = "🔴 BLOCKED" if risk > 0.5 else "🟢 ALLOWED"
        print(f"{status} (Risk: {risk:.2f}): {output[:50]}...")
    print()

    # Demo: Time well spent
    print(firewall.enforce_time_well_spent(130))
