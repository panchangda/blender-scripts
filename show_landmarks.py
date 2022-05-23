import bpy

# deselect all vertex
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')

# '\' means in python 
# so replace '\' with '\\`
# e.g. filepath = 'C:\\Users\\98329\\Desktop\\template.txt'
# or 
# use '/' as absolute path
filepath = 'C:/Users/98329/Desktop/template.txt'
# or 
# use r to ignore \
file = r'C:\Users\98329\Desktop\template.txt'
lines = []
with open(file,'r') as f:
    lines = f.readlines()  
     
# get rid of '\n' and so on
lines = [line.strip() for line in lines]

# select landmarks in lines
for i in lines:
    print(landmark)
for i in lines:
    obj.data.vertices[i].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 