# =================================================================================================================================
# EI EXTRA HELPER [ v1.2 ]
# =================================================================================================================================
# Author: Oleg <Knight Rider> Tolmachev.
# This python extension for Blender contains few useful functions for the ease of work with imported models from the Evil Islands game.
# It allows:
# 1) EI Copy Materials ~ assigns material from the base model to its morphs.
# 2) EI Copy UVs ~ copies UVs from the base model to its morphs.
# 3) EI Make Smooth ~ adds predefined subdivs for the easy smoothing.
# 4) EI Prepare ~ prepares model for smoothing (converts tris to quads, adds subdiv and triangulate modifiers).
# 5) EI Remove Multires ~ removes multires modifier from all.

# Note: for all of those actions above all collections should be enabled.
# To find those functions use Blender search after adding the extension.

# 6) EI HideAllCollectionsExceptBase ~ hides all the collections except base.
# 7) EI UnhideAllCollections ~ unhides all the collections.

# Function below should be applied to human resources only: 
# 8) EI HideAllExceptHumanBody ~ hides all the objects except human body parts.
# 8) EI HideAllExceptHumanBodyInBase ~ hides all the objects except human body parts in base collection.

# 9) EI UnhideAll ~ unhides all the objects on scene.
# 10) EI HideArmor ~ hides all the armor objects on scene.
# 11) EI UnhideArmor ~ unhides all the armor objects on scene.

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
    'version': (1, 2),
    'blender': (3, 0, 0),
    'location': '',
    'description': 'Evil Islands extra addon',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Object'}

# =================================================================================================================================
# HideAllCollectionsExceptBase

def hide_collection(collection_name):    
    if collection_name in bpy.context.view_layer.layer_collection.children:
        collection = bpy.context.view_layer.layer_collection.children[collection_name]
        collection.exclude = True          
            
def HideAllCollectionsExceptBase():
    hide_collection("str")
    hide_collection("dex")
    hide_collection("unique")
    hide_collection("base(scaled)")
    hide_collection("str(scaled)")
    hide_collection("dex(scaled)")
    hide_collection("unique(scaled)")    
    
class EIHideAllCollectionsExceptBase(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_hide_all_collections_except_base"
    bl_label = "EI Hide All Collections Except Base"
    bl_description = "Hides all collections except base"
    
    def execute(self, context):
        HideAllCollectionsExceptBase()
        return {'FINISHED'} 
 
# =================================================================================================================================
# HideAllExceptHumanBody 
    
def UnhideAllCollections():
    for collection in bpy.context.view_layer.layer_collection.children:
        collection.exclude = False
        
class EIUnhideAllCollections(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_unhide_all_collections"
    bl_label = "EI Unhide All Collections"
    bl_description = "Unhides all collections"
    
    def execute(self, context):
        UnhideAllCollections()
        return {'FINISHED'}   
 
# =================================================================================================================================
# HideAllExceptHumanBody
      
def HideAllExceptHumanBody():
    except_names = [ "hp", "bd", "hd", "rh1", "rh2", "rh3", "lh1", "lh2", "lh3", "rl1", "rl2", "rl3", "ll1", "ll2", "ll3", "s~hp", "s~bd", "s~hd", "s~rh1", "s~rh2", "s~rh3", "s~lh1", "s~lh2", "s~lh3", "s~rl1", "s~rl2", "s~rl3", "s~ll1", "s~ll2", "s~ll3", "d~hp", "d~bd", "d~hd", "d~rh1", "d~rh2", "d~rh3", "d~lh1", "d~lh2", "d~lh3", "d~rl1", "d~rl2", "d~rl3", "d~ll1", "d~ll2", "d~ll3", "u~hp", "u~bd", "u~hd", "u~rh1", "u~rh2", "u~rh3", "u~lh1", "u~lh2", "u~lh3", "u~rl1", "u~rl2", "u~rl3", "u~ll1", "u~ll2", "u~ll3", "b~hp", "b~bd", "b~hd", "b~rh1", "b~rh2", "b~rh3", "b~lh1", "b~lh2", "b~lh3", "b~rl1", "b~rl2", "b~rl3", "b~ll1", "b~ll2", "b~ll3", "p~hp", "p~bd", "p~hd", "p~rh1", "p~rh2", "p~rh3", "p~lh1", "p~lh2", "p~lh3", "p~rl1", "p~rl2", "p~rl3", "p~ll1", "p~ll2", "p~ll3",
    "g~hp", "g~bd", "g~hd", "g~rh1", "g~rh2", "g~rh3", "g~lh1", "g~lh2", "g~lh3", "g~rl1", "g~rl2", "g~rl3", "g~ll1", "g~ll2", "g~ll3", "c~hp", "c~bd", "c~hd", "c~rh1", "c~rh2", "c~rh3", "c~lh1", "c~lh2", "c~lh3", "c~rl1", "c~rl2", "c~rl3", "c~ll1", "c~ll2", "c~ll3" ] 
    
    for obj in bpy.context.scene.objects:
        if obj.name not in except_names and not obj.name.startswith("hr") and not obj.name.startswith("s~hr") and not obj.name.startswith("d~hr") and not obj.name.startswith("u~hr") and not obj.name.startswith("b~hr") and not obj.name.startswith("p~hr") and not obj.name.startswith("g~hr") and not obj.name.startswith("c~hr"):
            obj.hide_viewport = True
            obj.hide_render = True
            
class EIHideAllExceptHumanBody(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_hide_all_except_human_body"
    bl_label = "EI Hide All Except Human Body"
    bl_description = "Hides all the objects except human body"
    
    def execute(self, context):
        HideAllExceptHumanBody()
        return {'FINISHED'}            
            
def HideAllExceptHumanBodyInBase():
    except_names = [ "hp", "bd", "hd", "rh1", "rh2", "rh3", "lh1", "lh2", "lh3", "rl1", "rl2", "rl3", "ll1", "ll2", "ll3" ] 
    
    for obj in bpy.context.scene.objects:
        if obj.name not in except_names and not obj.name.startswith("hr"):
            obj.hide_viewport = True
            obj.hide_render = True

class EIHideAllExceptHumanBodyInBase(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_hide_all_except_human_body_in_base"
    bl_label = "EI Hide All Except Human Body In Base"
    bl_description = "Hides all the objects except human body in base collection"
    
    def execute(self, context):
        HideAllExceptHumanBodyInBase()
        return {'FINISHED'}

# =================================================================================================================================
# UnhideAll
  
def UnhideAll():  
    for obj in bpy.context.scene.objects:
        obj.hide_viewport = False
        obj.hide_render = False  

class EIUnhideAll(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_unhide_all"
    bl_label = "EI Unhide All"
    bl_description = "Unhides all the objects"
    
    def execute(self, context):
        UnhideAll()
        return {'FINISHED'}
        
# =================================================================================================================================
# HideArmor        
        
def HideArmor():
    
    for obj in bpy.data.objects:
        if ".armor" in obj.name:
            obj.hide_viewport = True  # Hide in viewport
            obj.hide_render = True    # Hide in renders
            
class EIHideArmor(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_hide_armor"
    bl_label = "EI Hide Armor"
    bl_description = "Hides all the armor objects"
    
    def execute(self, context):
        HideArmor()
        return {'FINISHED'}

def UnhideArmor():
    
    for obj in bpy.data.objects:
        if ".armor" in obj.name:
            obj.hide_viewport = False  # Show in viewport
            obj.hide_render = False    # Show in renders
            
class EIUnhideArmor(bpy.types.Operator):
    """    """
    bl_idname = "object.ei_unhide_armor"
    bl_label = "EI Unhide Armor"
    bl_description = "Unhides all the armor objects"
    
    def execute(self, context):
        UnhideArmor()
        return {'FINISHED'}
        
# =================================================================================================================================
# Prepare

# Prepares the model for smoothing. This includes:
#   ~ converting tris to quads
#   ~ adding multires
#   ~ adding ttriangulation
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
    EIHideAllExceptHumanBody,
    EIHideAllExceptHumanBodyInBase,
    EIUnhideAll,
    EIHideAllCollectionsExceptBase,
    EIUnhideAllCollections,
    EIHideArmor,
    EIUnhideArmor
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
    
def menu_func6(self, context):
    self.layout.operator(EIHideAllExceptHumanBody.bl_idname, text=EIHideAllExceptHumanBody.bl_label)
    
def menu_func7(self, context):
    self.layout.operator(EIHideAllExceptHumanBodyInBase.bl_idname, text=EIHideAllExceptHumanBodyInBase.bl_label)    
    
def menu_func8(self, context):
    self.layout.operator(EIUnhideAll.bl_idname, text=EIUnhideAll.bl_label)
    
def menu_func9(self, context):    
    self.layout.operator(EIHideAllCollectionsExceptBase.bl_idname, text=EIHideAllCollectionsExceptBase.bl_label)   

def menu_func10(self, context):
    self.layout.operator(EIUnhideAllCollections.bl_idname, text=EIUnhideAllCollections.bl_label)  

def menu_func11(self, context):    
    self.layout.operator(EIHideArmor.bl_idname, text=EIHideArmor.bl_label)   

def menu_func12(self, context):
    self.layout.operator(EIUnhideArmor.bl_idname, text=EIUnhideArmor.bl_label)      
    

def register():  
    for operator in bl_operators:
        print('reg operator: ' + str(operator))
        register_class(operator)
    
    bpy.types.VIEW3D_MT_object.append(menu_func1)
    bpy.types.VIEW3D_MT_object.append(menu_func2)
    bpy.types.VIEW3D_MT_object.append(menu_func3)
    bpy.types.VIEW3D_MT_object.append(menu_func4)
    bpy.types.VIEW3D_MT_object.append(menu_func5)
    bpy.types.VIEW3D_MT_object.append(menu_func6)
    bpy.types.VIEW3D_MT_object.append(menu_func7)
    bpy.types.VIEW3D_MT_object.append(menu_func8)
    bpy.types.VIEW3D_MT_object.append(menu_func9)
    bpy.types.VIEW3D_MT_object.append(menu_func10)
    bpy.types.VIEW3D_MT_object.append(menu_func11)
    bpy.types.VIEW3D_MT_object.append(menu_func12)
    
def unregister():
    for operator in bl_operators:
        unregister_class(operator)

if __name__ == '__main__':
    register()