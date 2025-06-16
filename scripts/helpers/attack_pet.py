t = Target.PromptTarget("Select enemy", 48)
if t:
    Player.InvokeVirtue("Honor")
    Target.WaitForTarget(3000, True)
    Target.TargetExecute(t)

    if Player.Followers > 0:
        Player.ChatSay(48, "All kill")
        Target.WaitForTarget(3000, True)
        Target.TargetExecute(t)
    
    Player.Attack(t)