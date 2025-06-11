using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

enemy_tracker := class(creative_device):
    # List of enemy spawners
    @editable
    Spawners : []npc_spawner_device = array{}
    
    # Lock device to control
    @editable
    LockDevice : lock_device = lock_device{}
    
    # Counter for active enemies
    var ActiveEnemiesCount : int = 0
    
    OnBegin<override>()<suspends>:void =
        # Subscribe to spawn and elimination events for all spawners
        for spawner in Spawners:
            if(spawner?):
                spawner.SpawnedEvent.Subscribe(OnEnemySpawned)
                spawner.EliminatedEvent.Subscribe(OnEnemyEliminated)
    
    OnEnemySpawned(Agent: agent):void =
        # Increment active enemies counter
        set ActiveEnemiesCount = ActiveEnemiesCount + 1
        Print("Enemigo spawn! Total: {ActiveEnemiesCount}")
    
    OnEnemyEliminated(Result: device_ai_interaction_result):void =
        # Decrement active enemies counter
        set ActiveEnemiesCount = ActiveEnemiesCount - 1
        Print("Enemigo eliminado! Restantes: {ActiveEnemiesCount}")
        
        # Check if all enemies are eliminated
        if(ActiveEnemiesCount <= 0):
            # Get the source agent (player who eliminated the enemy)
            if(SourceAgent := Result.Source?):
                # Open the lock with the source agent
                LockDevice.Open(SourceAgent)
                Print("¡Todos los enemigos eliminados! Puerta abierta por {SourceAgent.GetPlayerName()}.") 