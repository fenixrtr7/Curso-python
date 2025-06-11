using { FortniteGame }
using { FortniteGame.Player }

player_stats := class(creative_device):
    # Player reference
    PlayerRef : ?player = none
    
    # Stats modification values
    @editable
    HealthAmount : float = 25.0
    
    @editable
    SpeedMultiplier : float = 1.5
    
    @editable
    EnergyAmount : float = 50.0
    
    @editable
    ShieldAmount : float = 25.0
    
    # Trigger reference
    TriggerRef : ?trigger_device = none
    
    OnBegin<override>()<suspends>:void =
        # Get the trigger reference
        set TriggerRef = option{GetTrigger()}
        
        # Subscribe to trigger events
        if(trigger := TriggerRef?):
            trigger.TriggeredEvent.Subscribe(OnTriggered)
    
    OnTriggered()<suspends>:void =
        # Get the triggering player
        if(player := GetTriggeringPlayer()?):
            set PlayerRef = option{player}
            ModifyPlayerStats()
    
    ModifyPlayerStats()<suspends>:void =
        if(player := PlayerRef?):
            # Modify health
            player.SetHealth(player.GetHealth() + HealthAmount)
            
            # Modify speed
            player.SetSpeedMultiplier(SpeedMultiplier)
            
            # Modify energy
            player.SetEnergy(player.GetEnergy() + EnergyAmount)
            
            # Modify shields
            player.SetShield(player.GetShield() + ShieldAmount)
            
            # Print feedback
            Print("Stats modificados para: {player.GetPlayerName()}") 