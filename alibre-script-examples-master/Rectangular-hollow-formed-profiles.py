#https://help.alibre.com/articles/#!alibre-help-v23/rectangular-hollow-formed-profiles

# Rectangular hollow hot and cold formed profiles according to BS/EN-10210-2:1997 and BS/EN-10219:1997
 
# Measurements table H,B,T,ro,ri from here http://www.roymech.co.uk/Useful_Tables/Sections/RHS_cf.html
 
from collections import OrderedDict
 
 
PData = 0
 
HData = {}
HData[50.0]={}
HData[50.0][25.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0]
HData[50.0][30.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0]
HData[60.0]={}
HData[60.0][40.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3]
HData[76.2]={}
HData[76.2][50.8]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[80.0]={}
HData[80.0][40.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[90.0]={}
HData[90.0][50.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[100.0]={}
HData[100.0][50.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[100.0][60.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[120.0]={}
HData[120.0][60.0]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 12.0, 8.0]
HData[120.0][80.0]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0]
HData[140.0]={}
HData[140.0][80.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0]
HData[150.0]={}
HData[150.0][100.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[160.0]={}
HData[160.0][80.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[180.0]={}
HData[180.0][100.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[200.0]={}
HData[200.0][100.0]=[4.0, 7.5, 5.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[200.0][120.0]=[6.0, 9.45, 6.3],[6.3, 12.0, 8.0],[8.0, 15.0, 10.0],[10.0, 18.0, 12.0],[12.0, 18.75, 12.5],[12.5, 24.0, 16.0]
HData[250.0]={}
HData[250.0][150.0]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[260.0]={}
HData[260.0][180.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[300.0]={}
HData[300.0][200.0]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[350.0]={}
HData[350.0][250.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[400.0]={}
HData[400.0][200.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[450.0]={}
HData[450.0][250.0]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[500.0]={}
HData[500.0][300.0]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0],[20.0, 30.0, 20.0]
 
CData = {}
CData[40.0]={}
CData[40.0][20.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[50.0]={}
CData[50.0][25.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[50.0][30.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0]
CData[60.0]={}
CData[60.0][40.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[70.0]={}
CData[70.0][50.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[80.0]={}
CData[80.0][40.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[80.0][60.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[90.0]={}
CData[90.0][50.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[100.0]={}
CData[100.0][40.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[100.0][50.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[100.0][60.0]=[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[100.0][80.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[120.0]={}
CData[120.0][60.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[120.0][80.0]=[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[140.0]={}
CData[140.0][80.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[150.0]={}
CData[150.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[160.0]={}
CData[160.0][80.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[180.0]={}
CData[180.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[200.0]={}
CData[200.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[200.0][120.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[250.0]={}
CData[250.0][100.0]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.5, 37.5, 25.0]
CData[250.0][150.0]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[260.0]={}
CData[260.0][180.0]=[5.0, 10.0, 5.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0]={}
CData[300.0][100.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0][150.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0][200.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[350.0]={}
CData[350.0][250.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[400.0]={}
CData[400.0][200.0]=[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[400.0][300.0]=[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
 
 
#--- INPUT HERE ---#
print('Select hot or cold formed profiles')
print('0 = Hot\n1 = Cold')
HorC = int(Read())
 
if HorC == 0:
    PData = OrderedDict(sorted(HData.items(), key=lambda t: t[0]))
else:
    PData = OrderedDict(sorted(CData.items(), key=lambda t: t[0]))
 
print('Please select height')
for i,j in enumerate(PData):
    print i,'-',j,'mm'
     
readH = int(Read())
Size = PData.keys()[readH]
WData = PData[Size]
 
print('Please select width')
for i,j in enumerate(WData):
    print i,'-',j,'mm'
     
readW = int(Read())
Width = WData.keys()[readW]
 
 
print('Please select thickness')
for i,j in enumerate(WData[Width]):
    print i,'-',j[0],'mm'
 
readTh = int(Read())
 
Thick = WData[Width][readTh][0]
ro = WData[Width][readTh][1]
ri = WData[Width][readTh][2]
 
print('Please input length in mm')
Length = float(Read())
#--- INPUT STOP ---#
 
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
 
# Create part
Square = Part('Hollow Section %dx%dx%dx%d' % (Size,Width,Thick,Length))
 
# Body
Profile = Square.AddSketch('Profile', Square.GetPlane('XY-Plane'))
# Outer square
Line = Polyline()
Line.AddPoint(PolylinePoint(-Width/2.,-Size/2.))
Line.AddPoint(PolylinePoint(Width/2.,-Size/2.))
Line.AddPoint(PolylinePoint(Width/2.,Size/2.))
Line.AddPoint(PolylinePoint(-Width/2.,Size/2.))
Line.AddPoint(PolylinePoint(-Width/2.,-Size/2.))
Profile.AddPolyline(Line,False)
 
# Inner Square
Line = Polyline()
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(-Size/2.)+Thick))
Line.AddPoint(PolylinePoint((Width/2.)-Thick,(-Size/2.)+Thick))
Line.AddPoint(PolylinePoint((Width/2.)-Thick,(Size/2.)-Thick))
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(Size/2.)-Thick))
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(-Size/2.)+Thick))
Profile.AddPolyline(Line,False)
 
# Extrude
Square.AddExtrudeBoss('Extrude',Profile,Length,False)
 
# Outer radius
Square.AddFillet('Fillet<1>',[Square.GetEdge('Edge<6>'),Square.GetEdge('Edge<2>'),Square.GetEdge('Edge<4>'),Square.GetEdge('Edge<9>')],ro,False)
 
# Inner radius
Square.AddFillet('Fillet<2>',[Square.GetEdge('Edge<30>'),Square.GetEdge('Edge<31>'),Square.GetEdge('Edge<33>'),Square.GetEdge('Edge<35>')],ri,False)


