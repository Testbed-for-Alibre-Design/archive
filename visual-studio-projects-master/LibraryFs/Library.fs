
namespace LibraryFs
open System
open System.Runtime.InteropServices
open AlibreX
module CodeTest =
    let mutable hook : IAutomationHook = null
    try
        let activeObject = Marshal.GetActiveObject("AlibreX.AutomationHook")
        hook <- activeObject :?> IAutomationHook
        Console.WriteLine("Connected to Alibre.")
        let mutable root = hook.Root :?> IADRoot
        let session = root.Sessions.Count
        Console.WriteLine(session)
        Console.WriteLine(root.AppTitle)
        Console.WriteLine(root.Version)
        Console.WriteLine(root.Type)
        let session = root.Sessions
        for item in session do
            Console.WriteLine(item.Name)
        Console.WriteLine(session.Item(0).FilePath)
        hook <- null
        root <- null
    with
    | _ -> Console.WriteLine("Failed to connect to Alibre.")


