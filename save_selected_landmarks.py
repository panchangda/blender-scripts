import bpy
import bmesh

landmarks = []
obj=bpy.context.object
if obj.mode == 'EDIT':
    bm=bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if v.select:
            print(v)
            landmarks.append(v.index)
else:
    print("Object is not in edit mode.")

outputfile = r'C:\Users\98329\Desktop\source.txt';
first = True
with open(outputfile,'w') as f:
    for i in landmarks:
        if first:
            first = False
        else:
            f.write('\n')
        f.write(str(i))