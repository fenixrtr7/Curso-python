using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Verse.org/Simulation/Tags }

CoinTag := class(tag){}

coin_respawn_system := class(creative_device):
    # List of collectible coins
    @editable
    Coins : []collectible_object_device = array{}
    
    # Timer device
    @editable
    RespawnTimer : timer_device = timer_device{}
    
    # Respawn time in seconds
    @editable
    RespawnTime : float = 30.0
    
    # Counter for collected coins
    var CollectedCoinsCount : int = 0
    
    OnBegin<override>()<suspends>:void =
        # Subscribe to collection events for all coins
        for coin in Coins:
            if(coin?):
                coin.CollectedEvent.Subscribe(OnCoinCollected)
        
        # Subscribe to timer completion
        RespawnTimer.TimerFinishedEvent.Subscribe(OnTimerFinished)
    
    OnCoinCollected(Agent: agent):void =
        # Increment collected coins counter
        set CollectedCoinsCount = CollectedCoinsCount + 1
        
        # Check if all coins are collected
        if(CollectedCoinsCount >= Coins.Length):
            # Start the respawn timer
            RespawnTimer.Start(RespawnTime)
            Print("Todas las monedas recolectadas! Timer iniciado.")
    
    OnTimerFinished():void =
        # Reset all coins
        for coin in Coins:
            if(coin?):
                coin.Respawn()
        
        # Reset collected coins counter
        set CollectedCoinsCount = 0
        Print("Monedas respawneadas!") 