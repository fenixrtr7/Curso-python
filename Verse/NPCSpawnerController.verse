using { FortniteGame }
using { FortniteGame.NPCSpawner }
using { FortniteGame.Trigger }

npc_controller := class(creative_device):
    # List of NPC spawners to control
    Spawners : []npc_spawner_device = array{}
    
    # Trigger references for activation and deactivation
    ActivateTriggerRef : ?trigger_device = none
    DeactivateTriggerRef : ?trigger_device = none
    
    # Called when the device is spawned
    OnBegin<override>()<suspends>:void =
        # Get the trigger references
        set ActivateTriggerRef = option{GetTrigger(0)}
        set DeactivateTriggerRef = option{GetTrigger(1)}
        
        # Subscribe to trigger events
        if(trigger := ActivateTriggerRef?):
            trigger.TriggeredEvent.Subscribe(OnActivateTriggered)
        
        if(trigger := DeactivateTriggerRef?):
            trigger.TriggeredEvent.Subscribe(OnDeactivateTriggered)
    
    # Called when the activate trigger is activated
    OnActivateTriggered()<suspends>:void =
        # Activate all NPC spawners in the list
        for spawner in Spawners:
            if(spawner?):
                spawner.Activate()
    
    # Called when the deactivate trigger is activated
    OnDeactivateTriggered()<suspends>:void =
        # Deactivate all NPC spawners in the list
        for spawner in Spawners:
            if(spawner?):
                spawner.Deactivate() 