from orca import ActorState, Handoff, OrcaEvaluator

def coherent_case():
    actors = [
        ActorState("A",1.00,"B",12),
        ActorState("B",1.02,"B",12),
        ActorState("C",0.99,"B",11),
    ]
    handoffs = [
        Handoff("A","B","T1",True,True,True,True),
        Handoff("B","C","T2",True,True,True,True)
    ]
    return actors,handoffs,0,4

def degraded_case():
    actors = [
        ActorState("A",1.0,"A",12),
        ActorState("B",1.6,"B",8),
        ActorState("C",0.4,"C",6),
    ]
    handoffs = [
        Handoff("A","B","T1",True,False,False,True),
        Handoff("B","C","T2",False,True,False,False)
    ]
    return actors,handoffs,3,4

if __name__ == "__main__":
    ev = OrcaEvaluator()
    for label,case in [("coherent",coherent_case()),("degraded",degraded_case())]:
        print(label, ev.evaluate(*case))
