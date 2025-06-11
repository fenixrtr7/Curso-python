using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Verse.org/Simulation/Tags}

CoinTag := class(tag){}

CustomCallbackHandler := class():
    Manager : coin_device 
    Collectible : collectible_object_device
    HandlerFunction(Agent:agent):void=
        spawn{Manager.OnCollectedEvent(Agent, Collectible)}

coin_device := class(creative_device):

    @editable
    Accolade : accolades_device = accolades_device{}
    @editable
    RespawnTime : float = 60.0
    @editable
    Gold : item_granter_device  = item_granter_device {}

    OnBegin<override>()<suspends>:void=
        AccoladeConfiguration()

    AccoladeConfiguration() : void =
        TaggedActors := FindCreativeObjectsWithTag(CoinTag{})
        for(TaggedActor : TaggedActors, Coin := collectible_object_device[TaggedActor]):
            Coin.CollectedEvent.Subscribe(CustomCallbackHandler{Manager:=Self, Collectible:=Coin}.HandlerFunction)

    OnCollectedEvent(Agent:agent, Collectible:collectible_object_device)<suspends> : void =
        Print("Award")
        Accolade.Award(Agent)
        Gold.GrantItem(Agent)
        Sleep(RespawnTime)
        Collectible.Respawn(Agent)