# =================================================================================================================================
# EI EXTRA HELPER [ v1.1 ]
# =================================================================================================================================
# Author: Oleg <Knight Rider> Tolmachev.
# This python extension for Blender contains few useful functions for the ease of work with imported models from the Evil Islands game.
# It allows:
# 1) EI Copy Materials - assigns material from the base model to its morphs.
# 2) EI Copy UVs - copies UVs from the base model to its morphs.
# 3) EI Make Smooth - adds predefined subdivs for the easy smoothing.
# 4) EI Prepare - prepares model for smoothing (converts tris to quads, adds subdiv and triangulate modifiers).
# 5) EI Remove Multires - removes multires modifier from all.
# Note: for all of those actions all collections should be enabled.
# To find those functions use Blender search after adding the extension.
# =================================================================================================================================

import math
import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class

# =================================================================================================================================
# Info
bl_info = {
    'name': 'EI Extra Helper',
    'author': 'OKRT',
    'version': (1, 1),
    'blender': (3, 0, 0),
    'location': '',
    'description': 'Evil Islands extra addon',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Object'}
    
# =================================================================================================================================
# Prepare

# Prepares the model for smoothing. This includes:
#   - converting tris to quads
#   - adding multires
#   - adding ttriangulation
def PrepareModel():
    
    face_threshold = math.radians(40)
    shape_threshold = math.radians(40)
    
    # iterate through all the models and make them smooth
    for obj in bpy.data.objects:
        if obj.hide_viewport:
            continue            
        
        try:        
            bpy.context.view_layer.objects.active = obj  
            if bpy.context.view_layer.objects.active is None:
                continue  
        
            if obj.type == 'MESH': 
                #scene.objects.active = obj # set active object
                bpy.ops.object.mode_set(mode='EDIT') # switch to edit mode
                for vert in obj.data.vertices:                
                    vert.select = True # ensure all vertices are selected                 
            
                #bpy.ops.mesh.tris_convert_to_quads(face_threshold=face_threshold, shape_threshold=shape_threshold)
                bpy.ops.mesh.tris_convert_to_quads(face_threshold=face_threshold, shape_threshold=shape_threshold, uvs=True, seam=True)
                bpy.ops.mesh.delete_loose() # delete loose geometry
                bpy.ops.mesh.dissolve_degenerate() # 
                bpy.ops.mesh.remove_doubles() # remove doubles            
                bpy.ops.object.mode_set(mode='OBJECT') # switch to object mode
            
                mod = obj.modifiers.new("Subdivision", 'SUBSURF')
            
            
                #mod = obj.modifiers.new("Multires", 'MULTIRES')
                #bpy.ops.object.multires_subdivide(modifier="Multires", mode='LINEAR')
                #bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
                mod = obj.modifiers.new("Triangulate", 'TRIANGULATE') 
                mod.show_viewport = False
        except:
            print(obj.name)

class EIPrepare(bpy.types.Operator):
    """This allows to prepare model for smoothing"""
    bl_idname = "object.ei_prepare"
    bl_label = "EI Prepare"
    bl_description = "Prepares the model for smoothing"
    
    def execute(self, context):
        PrepareModel()
        return {'FINISHED'}
        
# =================================================================================================================================
# Remove Multires

# Removes multiresolution from all the visible objects
def RemoveMultires():    
    # iterate through all the models and remove multisresolution
    for obj in bpy.data.objects:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_remove(modifier="Multires")
        
class EIRemoveMultires(bpy.types.Operator):
    """This allows to remove multiresolution from all the models"""
    bl_idname = "object.ei_remove_multires"
    bl_label = "EI Remove Multires"
    bl_description = "Removes multiresolution modifier from all the visible objects"
    
    def execute(self, context):
        RemoveMultires()
        return {'FINISHED'}
    
    
# =================================================================================================================================
# Make Smooth
            
# Makes smooth all the models a simple way
def MakeSmooth4All():
    
    # iterate through all the models and make them smooth
    for obj in bpy.data.objects:
        bpy.context.view_layer.objects.active = obj
        mod = obj.modifiers.new("Multires", 'MULTIRES')
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')
        mod.show_viewport = False

class EIMakeSmooth(bpy.types.Operator):
    """This allows to make smooth all the models"""
    bl_idname = "object.ei_make_smooth"
    bl_label = "EI Make Smooth"
    bl_description = "Makes smooth all the models"
    
    def execute(self, context):
        MakeSmooth4All()
        return {'FINISHED'}
    
# =================================================================================================================================
def PrepareLinkToActive(func):
    
    # deselect all the objects at start
    bpy.ops.object.select_all(action='DESELECT')
    
    # get the count of actual models from the base collection
    count = len(bpy.data.collections['base'].all_objects)
    print('Total count of models =', count)
    
    # iterate through all the base models, select their morphs respectively and join UVs
    for i in range(count):  
        
        # take the current base model
        baseobj = bpy.data.collections['base'].all_objects[i]        
        
        # iterate through all the collections except the base one
        for collection in bpy.data.collections:
            if collection.name == 'base':
                continue
            
            # take the current morph model
            obj = collection.all_objects[i]
            obj.select_set(True)
            print(collection.name, obj.name)
            
        # set the active object
        bpy.context.view_layer.objects.active = baseobj
        print('base', baseobj.name)
        
        # func
        func()  
        
        # deselect all the objects
        bpy.ops.object.select_all(action='DESELECT')   
    
    
# =================================================================================================================================
# Copy UVs
        
# Copies UVs from the base models to their morphs
def CopyUVs():  
    
    PrepareLinkToActive(bpy.ops.object.join_uvs)
        

class EICopyUVs(bpy.types.Operator):
    """This allows to copy UVs from the base model to its morphs"""
    bl_idname = "object.ei_copy_uvs"
    bl_label = "EI Copy UVs"
    bl_description = "Copies UVs from the base model to its morphs"
    
    def execute(self, context):
        CopyUVs()
        return {'FINISHED'}
    
# =================================================================================================================================
# Copy Materials
        
# Copies materials from the base models to their morphs
def CopyMaterials():  
    
    PrepareLinkToActive(bpy.ops.object.material_slot_copy)
        

class EICopyMaterials(bpy.types.Operator):
    """This allows to copy materials from the base model to its morphs"""
    bl_idname = "object.ei_copy_materials"
    bl_label = "EI Copy Materials"
    bl_description = "Copies materials from the base model to its morphs"
    
    def execute(self, context):
        CopyMaterials()
        return {'FINISHED'}

# =================================================================================================================================
# Registration

bl_operators = (
    EICopyUVs,
    EIMakeSmooth,
    EICopyMaterials,
    EIPrepare,
    EIRemoveMultires,
)

def menu_func1(self, context):
    self.layout.operator(EICopyUVs.bl_idname, text=EICopyUVs.bl_label)
    
def menu_func2(self, context):
    self.layout.operator(EIMakeSmooth.bl_idname, text=EIMakeSmooth.bl_label)
    
def menu_func3(self, context):
    self.layout.operator(EICopyMaterials.bl_idname, text=EICopyMaterials.bl_label)
    
def menu_func4(self, context):
    self.layout.operator(EIPrepare.bl_idname, text=EIPrepare.bl_label)
    
def menu_func5(self, context):
    self.layout.operator(EIRemoveMultires.bl_idname, text=EIRemoveMultires.bl_label)

def register():  
    for operator in bl_operators:
        print('reg operator: ' + str(operator))
        register_class(operator)
    
    bpy.types.VIEW3D_MT_object.append(menu_func1)
    bpy.types.VIEW3D_MT_object.append(menu_func2)
    bpy.types.VIEW3D_MT_object.append(menu_func3)
    bpy.types.VIEW3D_MT_object.append(menu_func4)
    bpy.types.VIEW3D_MT_object.append(menu_func5)
    
def unregister():
    for operator in bl_operators:
        unregister_class(operator)

if __name__ == '__main__':
    register()