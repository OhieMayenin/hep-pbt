import pyg4ometry 
import pyg4ometry.geant4.Material

def completeModel() : 
    # define local materials dict
    lmd = materials()

    # make a material dictionary 
    # pyg4ometry.freecad.Gdml.MakeMaterialDict()

    # create a dictionary of materials 
    md  = pyg4ometry.freecad.Gdml.LoadMaterialDict("./ClatterbridgeSTEP_Simplified.mat",lmd)

    # create a visualisation macro based on material
    # pyg4ometry.freecad.Gdml.MakeVisMacro()

    # convert model
    pyg4ometry.freecad.Gdml.DocumentToGdml(md)

def materials() : 
    element_h  = pyg4ometry.geant4.Element.simple("Hydrogen","H",1,1.01)
    element_o  = pyg4ometry.geant4.Element.simple("Oxygen","O",8,16.00)
    element_c  = pyg4ometry.geant4.Element.simple("Carbon","C",6,12.01)
    
    pmma = pyg4ometry.geant4.Material.composite("PMMA",1.19,3)
    pmma.add_element_natoms(element_h,8)
    pmma.add_element_natoms(element_o,2)
    pmma.add_element_natoms(element_c,5)

    return {"PMMA":pmma}
    
