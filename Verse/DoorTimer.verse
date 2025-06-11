using { FortniteGame }
using { FortniteGame.Door }

door := class(creative_device):
    # Door reference
    DoorRef : door = none
    
    # Timer variables
    TimerActive : bool = false
    TimeRemaining : float = 60.0
    
    # Called when the device is spawned
    OnBegin<override>()<suspends>:void =
        # Get the door reference
        DoorRef := GetDoor()
        if(DoorRef != none):
            # Subscribe to door events
            DoorRef.OnDoorOpened.Subscribe(OnDoorOpened)
            DoorRef.OnDoorClosed.Subscribe(OnDoorClosed)
    
    # Called when the door opens
    OnDoorOpened()<suspends>:void =
        if(!TimerActive):
            TimerActive := true
            TimeRemaining := 60.0
            StartTimer()
    
    # Called when the door closes
    OnDoorClosed()<suspends>:void =
        TimerActive := false
    
    # Timer function
    StartTimer()<suspends>:void =
        while(TimerActive and TimeRemaining > 0.0):
            TimeRemaining -= 1.0
            Sleep(1.0)
        
        if(TimerActive and DoorRef != none):
            DoorRef.Close()
            TimerActive := false
