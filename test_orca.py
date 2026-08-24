import unittest
from orca import ActorState, Handoff, OrcaEvaluator

class TestOrca(unittest.TestCase):
    def test_identical_state_high_consistency(self):
        ev = OrcaEvaluator()
        actors = [ActorState("A",1.0), ActorState("B",1.0)]
        self.assertAlmostEqual(ev.state_consistency(actors),1.0)

    def test_complete_handoff(self):
        ev = OrcaEvaluator()
        h = [Handoff("A","B","T",True,True,True,True)]
        self.assertAlmostEqual(ev.handoff_integrity(h),1.0)

    def test_degraded_coordination_scores_lower(self):
        ev = OrcaEvaluator()
        good = ev.evaluate(
            [ActorState("A",1.0,"A",5),ActorState("B",1.0,"A",5)],
            [Handoff("A","B","T",True,True,True,True)],
            0,2
        )
        bad = ev.evaluate(
            [ActorState("A",1.0,"A",5),ActorState("B",2.0,"B",1)],
            [Handoff("A","B","T",False,False,False,False)],
            2,2
        )
        self.assertGreater(good["coordination_score"], bad["coordination_score"])

if __name__ == "__main__":
    unittest.main()
