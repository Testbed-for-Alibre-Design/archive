<Query Kind="Program">
  <Reference>&lt;ProgramFilesX64&gt;\Alibre Design 26.0.0.26040\Program\AlibreX.dll</Reference>
  <Reference>&lt;RuntimeDirectory&gt;\Microsoft.VisualBasic.dll</Reference>
  <Reference>&lt;RuntimeDirectory&gt;\System.Windows.Forms.dll</Reference>
  <Namespace>AlibreX</Namespace>
  <Namespace>Microsoft.VisualBasic</Namespace>
  <Namespace>System</Namespace>
  <Namespace>System.Windows.Forms</Namespace>
  <Namespace>System.Runtime.InteropServices</Namespace>
</Query>
public IADSession Session;
public IADDesignSession objADDesignSession;
public IADDesignPlane objADDesignPlane;
public IADPartSession objADPartSession;
public IADSketches objADSketches;
public IADSketch objADSketch;
public IADSketchFigures objADSketchFigures;
public IADSketchLine objADSketchLine;
public IADSketchCircle circleSketch;
public IADSketchPoint pointSketch;
public IADSketchPoint objStartPoint;
public IADSketchPoint objEndPoint;
public double dblLength;
public double HIEGHT;
public double LENGTH;
public double THICKNESS;
public double WEB;
public double WEB_divided;
public double S1;
public double S2;
public double S3;
public double S4;
public double s1_divided;
public double s2_divided;
public double s3_divided;
public double s4_divided;
public IADSession session;
public IADExtrusionFeature extrusion;
public double Dimension;
public IAutomationHook Hook;
public IADRoot Root;
public double ID;
public double OD;
public void Main()
{
	Connection1();
	Root.Sessions.Count.Dump();
	Root.Sessions.Item(0).Name.Dump("name");
	if (Root.Sessions.Count != 0)
	{
		foreach (IADSession item in Root.Sessions)
		{
			item.Name.Dump();
			foreach (IADParameter item2 in item.Parameters)
			{
				item2.Name.Dump();
			}
			item.FilePath.Dump();
		}
	}
	else
	{
		//var out = "0".Dump();
	}
	Hook = null;
	Root = null;
}
public void Connection1()
{
	IAutomationHook hook;
	try
	{
		//Connecting to Alibre
		hook = (IAutomationHook)Marshal.GetActiveObject("AlibreX.AutomationHook");
		Root = hook.Root as IADRoot;
		Console.WriteLine("Connected to Alibre.");
	}
	catch
	{
		Console.WriteLine("Failed to connect to Alibre.");
	}
}
//public static IAutomationHook hook;
//public static IADRoot root;
//
//public void Connection2()
//{
//	hook = new AutomationHook();
//	hook.Initialize(null, null, null, false, 0);
//	root = hook.Root as IADRoot;
//
//}