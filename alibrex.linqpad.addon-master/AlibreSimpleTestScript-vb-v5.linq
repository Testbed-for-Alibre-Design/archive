<Query Kind="VBProgram">
  <Reference>&lt;ProgramFilesX64&gt;\Alibre Design 26.0.0.26040\Program\AlibreX.dll</Reference>
  <Reference>&lt;RuntimeDirectory&gt;\Microsoft.VisualBasic.dll</Reference>
  <Reference>&lt;RuntimeDirectory&gt;\System.Windows.Forms.dll</Reference>
  <Namespace>AlibreX</Namespace>
  <Namespace>Microsoft.VisualBasic</Namespace>
  <Namespace>System.Windows.Forms</Namespace>
</Query>

Public Session As IADSession
Public objADDesignSession As AlibreX.IADDesignSession
Public objADDesignPlane As AlibreX.IADDesignPlane
Public objADPartSession As AlibreX.IADPartSession
Public objADSketches As AlibreX.IADSketches
Public objADSketch As AlibreX.IADSketch
Public objADSketchFigures As AlibreX.IADSketchFigures
Public objADSketchLine As AlibreX.IADSketchLine
Public circleSketch As AlibreX.IADSketchCircle
Public pointSketch As AlibreX.IADSketchPoint
Public objStartPoint As AlibreX.IADSketchPoint
Public objEndPoint As AlibreX.IADSketchPoint
Public dblLength As Double
Public HIEGHT As Double
Public LENGTH As Double
Public THICKNESS As Double
Public WEB As Double
Public WEB_divided As Double
Public S1 As Double
Public S2 As Double
Public S3 As Double
Public S4 As Double
Public s1_divided As Double
Public s2_divided As Double
Public s3_divided As Double
Public s4_divided As Double
'Public session As IADSession
Public extrusion As IADExtrusionFeature
Public Dimension As Double
Public Hook As IAutomationHook
Public Root As IADRoot
Private Property Holebase As BindingSource
Dim ID As Double
Dim OD As Double

Sub Main()
	
	Connection1()

	'Root.Sessions.Count.Dump()
	Root.Sessions.Item(0).Name.Dump("name")
	'Root.Dump()
	If Root.Sessions.Count <> 0 Then


		For Each item As IADSession In Root.Sessions

		
			item.Name.Dump
			'item.ConstituentFilePaths.Dump

			For Each item2 As IADParameter In item.Parameters
				item2.Name.Dump
			Next

			item.FilePath.Dump

		Next
	Else
		Dim out = "0".dump
	End If
	'Session = Root.Sessions.Item(0)

	'WriteLine(Root.Sessions.Count)

	Hook = Nothing

	Root = Nothing

End Sub

' Define other methods and classes here



Sub Connection1()

	Hook = GetObject(, "AlibreX.AutomationHook")
	Root = Hook.Root

End Sub

Sub Connection2()
	Hook = New AlibreX.AutomationHook
	Call Hook.Initialize("", "", "", True, 0)
	Dim m_objADRoot As IADRoot
	m_objADRoot = Hook.Root
End Sub