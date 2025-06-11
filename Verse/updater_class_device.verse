using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Fortnite.com/Characters }

# See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.

# A Verse-authored creative device that can be placed in a level
updater_class_device := class(creative_device):

    #initializing an empty map
    var PlayerMap :[player]int = map{}

    @editable
    ClassSelectors : []class_and_team_selector_device = array{}

    @editable
    ConditionalButton : conditional_button_device = conditional_button_device{}

    @editable
    TriggerRef : trigger_device = trigger_device{}

    # Current index in the ClassSelectors array
    var CurrentSelectorIndex : int = 0

    # Runs when the device is started in a running game
    OnBegin<override>()<suspends>:void=
        ConditionalButton.ActivatedEvent.Subscribe(OnButton)
        TriggerRef.TriggeredEvent.Subscribe(OnTriggered)
        InitPlayers()        

    InitPlayers() : void=
        AllPlayers := GetPlayspace().GetPlayers()
        for (Player : AllPlayers, FortCharacter := Player.GetFortCharacter[]):
            if(set PlayerMap[Player] = 10, WeaponTier := PlayerMap[Player]):
                Print("Storing player")

    OnTriggered(Agent: ?agent):void =
        if(Agent? && (Player := Agent? as player) && (CurrentValue := PlayerMap[Player])):
            # Set the button's required item count to the player's current value
            ConditionalButton.SetItemCountRequired(0, CurrentValue)

    OnButton(Agent : agent):void=
        # Get current selector
        if(current_selector := ClassSelectors[CurrentSelectorIndex]):
            # Change class for the agent
            current_selector.ChangeClass(Agent)
            
            # Move to next selector in the list
            set CurrentSelectorIndex = (CurrentSelectorIndex + 1) 
            
            # Double the required item count
            # Get player and update their value in PlayerMap
            if(Agent as player as Player):
                if(CurrentValue := PlayerMap[Player]):
                    set PlayerMap[Player] = CurrentValue + 1