Imports AlibreX
Public Module Init
	Public Session As IADSession
	Public objADPartSession As IADPartSession
	Public Dimension As Double
	Public Hook As IAutomationHook
	Public Root As IADRoot
	Sub CodeTest()
		Hook = GetObject(, "AlibreX.AutomationHook")
		Root = Hook.Root
		Session = Root.Sessions.Item(0)
		objADPartSession = Session
		Dim b As IADBodies
		b = objADPartSession.Bodies
		Dim verts As IADVertices = b.Item(0).Vertices
		For i As Integer = 0 To verts.Count - 1
			printpoint(verts.Item(i).Point.X, verts.Item(i).Point.Y, verts.Item(i).Point.Z)
		Next
		Dim c As IADFaces
		c = b.Item(0).Faces
		For j As Integer = 0 To c.Count - 1
		Next
		Hook = Nothing
		Root = Nothing
	End Sub
	Sub printpoint(x, y, z)
		Console.WriteLine(x & " , " & y & " , " & z)
	End Sub
End Module
