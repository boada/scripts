
python sqlcl.py -q "SELECT TOP 1000 G.objID, GN.distance, G.ra, G.dec, G.u,G.g,G.r,G.i,G.z FROM Galaxy as G JOIN dbo.fGetNearbyObjEq(191.07625,16.79716,0.066) AS GN ON G.objID = GN.objID Where G.g < 22 ORDER BY distance" > out
