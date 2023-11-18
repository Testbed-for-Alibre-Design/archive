using AlibreX;
using System.Runtime.InteropServices;
using System;

namespace LibraryCs
{
    public class Init
    {
        public static IADSession Session;
        public static IADPartSession objADPartSession;
        public static IAutomationHook Hook;
        public static IADRoot Root;

        public static void CodeTest()
        {
            Hook = (IAutomationHook)Marshal.GetActiveObject("AlibreX.AutomationHook");
            Root = (IADRoot)Hook.Root;
            Session = Root.Sessions.Item(0);
            objADPartSession = (IADPartSession)Session;
            Console.WriteLine(Session.FilePath);
            Console.WriteLine(objADPartSession.Bodies.Count);
            IADBodies b = objADPartSession.Bodies;
            IADVertices verts = b.Item(0).Vertices;
            Console.WriteLine(verts.Count);
            for (int i = 0; i <= verts.Count - 1; i++)
            {
                Printpoint(verts.Item(i).Point.X, verts.Item(i).Point.Y, verts.Item(i).Point.Z);
            }
            IADFaces c = b.Item(0).Faces;
            for (int j = 0; j <= c.Count - 1; j++)
            {
            }
            Hook = null;
            Root = null;
        }

        public static void Printpoint(double x, double y, double z)
        {
            Console.WriteLine(x + " , " + y + " , " + z);
        }
    }
}