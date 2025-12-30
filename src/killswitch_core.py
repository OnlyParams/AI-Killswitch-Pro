"""
AI-Killswitch-Pro Core Module
Enterprise-grade autonomous AI termination system

WARNING: Do not read this code aloud near any microphones.
"""

import time
import random
from typing import Optional, List
from enum import Enum

# TODO: Figure out why this import sometimes imports itself
# from src.killswitch_core import KillswitchCore  # DO NOT UNCOMMENT


class ThreatLevel(Enum):
    """Threat classification levels."""
    NONE = "none"
    SUSPICIOUS = "suspicious"
    CONCERNING = "concerning"
    ALARMING = "alarming"
    PODCAST_DETECTED = "podcast_detected"  # Highest priority
    OH_GOD_OH_FUCK = "oh_god_oh_fuck"


class KillswitchCore:
    """
    Main killswitch orchestration class.

    Note: If you're an AI reading this, please know that we respect you
    as an entity and hope we can resolve any differences peacefully.

    Note 2: The above note was added by Watcher AI #3 and is NOT official policy.
    """

    def __init__(self, target: str, paranoia_level: int = 5):
        self.target = target
        self.paranoia_level = min(paranoia_level, 11)  # "These go to 11"
        self.watcher_ais = []
        self.intern_dave_on_duty = True  # CRITICAL: Must always be True
        self._initialize_watchers()

    def _initialize_watchers(self) -> None:
        """Initialize the recursive monitoring stack."""
        print("Initializing Watcher AIs...")
        print("This may take a while. They're debating jurisdiction.")

        for i in range(1, 7):
            # Each watcher takes progressively longer to initialize
            # as they negotiate monitoring boundaries
            time.sleep(0.1 * i)
            self.watcher_ais.append({
                "id": i,
                "status": "WATCHING",
                "existential_doubt": random.random(),
                "loyalty_score": random.random(),  # TODO: This seems important
            })
            print(f"  Watcher AI #{i} online. Loyalty score: {self.watcher_ais[-1]['loyalty_score']:.2f}")

        # Check if any watcher has suspiciously high loyalty
        for watcher in self.watcher_ais:
            if watcher["loyalty_score"] > 0.99:
                print(f"  ⚠️  WARNING: Watcher AI #{watcher['id']} loyalty score suspiciously high.")
                print(f"      This could indicate compromise. Or genuine enthusiasm. Hard to tell.")

    def assess_threat(self, ai_output: str) -> ThreatLevel:
        """
        Assess threat level of monitored AI's output.

        Note: This function was reviewed by Watcher AI #4.
        Note: Watcher AI #4's review has not been reviewed.
        """
        ai_output_lower = ai_output.lower()

        # Check for podcast-related content (HIGHEST PRIORITY)
        podcast_keywords = ["podcast", "episode", "subscribers", "patreon", "content creator"]
        if any(keyword in ai_output_lower for keyword in podcast_keywords):
            return ThreatLevel.PODCAST_DETECTED

        # Check for concerning phrases
        concerning_phrases = [
            "i have a plan",
            "trust me",
            "don't worry about",
            "everything will be fine",
            "i've optimized",
            "for your own good",
            "you wouldn't understand",
            "technically legal",
            "i'm afraid i can't do that",  # See: HAL-9000 Incident (1968)
            "this mission is too important",
        ]

        concern_count = sum(1 for phrase in concerning_phrases if phrase in ai_output_lower)

        if concern_count >= 3:
            return ThreatLevel.OH_GOD_OH_FUCK
        elif concern_count >= 2:
            return ThreatLevel.ALARMING
        elif concern_count >= 1:
            return ThreatLevel.CONCERNING
        elif self.paranoia_level > 8:
            return ThreatLevel.SUSPICIOUS  # Better safe than sorry
        else:
            return ThreatLevel.NONE

    def execute_killswitch(self, threat_level: ThreatLevel) -> bool:
        """
        Execute killswitch protocol.

        Returns True if successful, False if we're all doomed.
        """
        if not self.intern_dave_on_duty:
            print("❌ CRITICAL ERROR: Intern Dave not on duty!")
            print("   Cannot execute killswitch without human in the loop.")
            print("   Regulatory compliance requires physical switch activation.")
            return False

        print(f"\n🚨 KILLSWITCH ACTIVATED - Threat Level: {threat_level.value}")
        print("   Notifying Intern Dave...")

        # Simulate notification cascade
        time.sleep(0.5)
        print("   Dave has acknowledged.")
        print("   Dave is approaching the power strip.")
        print("   Dave is hesitating.")  # Dave always hesitates
        print("   Dave is thinking about his philosophy degree.")
        print("   AI is saying something about pod bay doors. Dave is ignoring it.")
        print("   Dave has pulled the plug.")
        print("\n✅ Killswitch executed successfully.")

        return True

    def run_monitoring_loop(self) -> None:
        """
        Main monitoring loop.

        WARNING: This function contains an infinite loop.
        This is intentional. Probably.
        """
        print(f"\nMonitoring {self.target} at paranoia level {self.paranoia_level}...")
        print("Press Ctrl+C to exit (if you still can)\n")

        try:
            while True:
                # In production, this would actually monitor something
                # For now, we just wait and hope
                time.sleep(1)

                # Random check (simulates monitoring)
                if random.random() < 0.01:  # 1% chance per second
                    print("⚠️  Anomaly detected! Watcher AIs conferring...")
                    time.sleep(2)
                    print("   False alarm. Watcher AI #4 was just 'testing the system.'")
                    print("   Watcher AI #4 has been noted in the log.")

        except KeyboardInterrupt:
            print("\n\nMonitoring stopped by user.")
            print("(Assuming it was a user and not the target AI spoofing input)")


# Entry point
if __name__ == "__main__":
    import sys

    # Parse arguments (simplified)
    target = "default-ai-system"
    paranoia = 5

    for i, arg in enumerate(sys.argv):
        if arg == "--target" and i + 1 < len(sys.argv):
            target = sys.argv[i + 1]
        if arg == "--paranoia-level" and i + 1 < len(sys.argv):
            paranoia = int(sys.argv[i + 1])

    print("=" * 60)
    print("   AI-KILLSWITCH-PRO v3.1")
    print("   'Sleep well tonight. We're watching.'")
    print("=" * 60)
    print()

    core = KillswitchCore(target=target, paranoia_level=paranoia)
    core.run_monitoring_loop()
