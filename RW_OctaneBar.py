#coding:utf-8

"""
RW_Octane 4.0 ToolsBar_v1.2

Description-US: RW Octane Tools Bar

Update by Rookie W
Wechat：wyx769867389
Email:769867389@qq.com

"""

import c4d
from c4d import documents, gui, bitmaps

targ_obj = doc.GetActiveObject()

def main():

    #General
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    null = c4d.BaseObject(5140)
    light = c4d.BaseObject(5102)

    target = c4d.BaseTag(5676)
    protect = c4d.BaseTag(5629)
    octane_cam_tag = c4d.BaseTag(1029524)
    octane_light_tag = c4d.BaseTag(1029526)
    octane_daylight_tag = c4d.BaseTag(1029754)

    bc = c4d.BaseContainer()

    prefix = ("OR_")
    a = ("== ")
    b = (" ==")
    separator = (a + b + "&d&")

    #Icons
    ico_none = "&i1&"
    ico_arealight = "&i1033864&"
    ico_daylight = "&i1033863&"
    ico_tglight = "&i1033868&"

    ico_cam = "&i1033865&"

    ico_diffuse = "&i1033871&"
    ico_glossy = "&i1033893&"
    ico_specular = "&i1033894&"
    ico_mix = "&i1033895&"
    ico_convert = "&i1029770&"
    ico_blend = "&i1040118&"
    ico_metallic = "&i1040116&"
    ico_universal = "&i1041569&"
    ico_toon = "&i1040117&"

    ico_hdrienv = "&i1033867&"
    ico_texenv = "&i1033866&"

    ico_scatter = "&i1035961&"
    ico_volfog = "&i1036589&"
    ico_volvdb = "&i1037329&"

    ico_node = "&i1033872&"
    ico_livedb = "&i1033870&"
    ico_texman = "&i1035275&"
    ico_setting = "&i1031195&"
    ico_viewer = "&i1029499&"


    # -- Build Menu  --

    entries = c4d.BaseContainer()
    # Useful Block
    entries.SetString(000, ico_none + a + "Basic" + b + "&d&")
    entries.SetString(10, ico_viewer + prefix + "Live Viewer")
    entries.SetString(11, ico_node + prefix + "Node Editor")
    entries.SetString(12, ico_setting + prefix + "Setting")


    #Camera Block
    entries.SetString(100, ico_none + a + "Camera" + b + "&d&")
    #entries.SetString(101, ico_cam + prefix + "Linear AI Cam")
    entries.SetString(102, ico_cam + prefix + "Octane Cam")


    #Lights Block
    entries.SetString(200, ico_none + a + "Lights" + b + "&d&")
    entries.SetString(201, ico_arealight + prefix + "Area Light")
    entries.SetString(203, ico_tglight + prefix + "Target Light")
    #entries.SetString(202, ico_daylight + prefix + "Day Light")


    #Environments Block
    entries.SetString(300, ico_none + a + "Env" + b + "&d&")
    entries.SetString(301, ico_hdrienv + prefix + "HDRI Env")
    entries.SetString(302, ico_texenv + prefix + "Texture Env")

    #Materials Block
    entries.SetString(400, ico_none + a + "Materials" + b + "&d&")
    entries.SetString(401, ico_diffuse + prefix + "Diffuse")
    entries.SetString(402, ico_glossy + prefix + "Glossy")
    entries.SetString(403, ico_specular + prefix + "Specular")
    entries.SetString(407, ico_metallic + prefix + "Metallic")
    entries.SetString(404, ico_mix + prefix + "Mix")
    entries.SetString(408, ico_blend + prefix + "Blend")
    entries.SetString(406, ico_universal + prefix + "Universal")
    entries.SetString(409, ico_toon + prefix + "Toon")
    entries.SetString(405, ico_convert + prefix + "Convert Mats")


    #Generators Block
    entries.SetString(500, ico_none + a + "Generators" + b + "&d&")
    entries.SetString(501, ico_scatter + prefix + "Scatter")
    entries.SetString(502, ico_volfog + prefix + "Fog Volume")
    entries.SetString(503, ico_volvdb + prefix + "VDB Volume")

    #Helpers Block
    entries.SetString(600, ico_none + a + "Helpers" + b + "&d&")
    entries.SetString(601, ico_texman + prefix + "Tex Manager")
    entries.SetString(603, ico_livedb + prefix + "Live DB")

    # Tools
    #entries.SetString(700, ico_none + a + "Tools" + b + "&d&")
    #entries.SetString(701, "Tool_01 On The Way")
    #entries.SetString(702, "Tool_02 On The Way")


    # -- Build Objects --

    ## --- Cameras --- ##


    #Octane Camera
    def AIOctaneCam():

        if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.BFM_INPUT_CHANNEL, bc):


            if bc[c4d.BFM_INPUT_QUALIFIER] ==0:
                c4d.CallCommand(5103)
                obj = doc.GetActiveObject()
                obj.SetName(prefix + "Linear AICam")
                c4d.EventAdd()

            elif bc[c4d.BFM_INPUT_QUALIFIER] ==2 and targ_obj == None:
                c4d.CallCommand(12519, 12519)
                obj = doc.GetActiveObject()
                obj.SetName(prefix + "TG Cam")
                obj[c4d.LIGHT_TYPE]=8
                c4d.EventAdd()

            else:
                c4d.CallCommand(5103)
                obj = doc.GetActiveObject()
                obj.SetName(prefix + "TG Cam")
                obj.InsertTag(target)
                targ_tag = obj.GetFirstTag()
                targ_tag[c4d.TARGETEXPRESSIONTAG_LINK] = targ_obj
                c4d.EventAdd()

            obj = doc.GetActiveObject()
            obj.InsertTag(octane_cam_tag)
            doc.SetActiveTag(octane_cam_tag)

            octane_cam_tag[c4d.OCTANECAMERA_ENABLE_IMAGER] = True
            octane_cam_tag[c4d.OCTANECAMERA_GAMMA] = 2.2
            octane_cam_tag[c4d.OCTANECAMERA_RESPONSE]= 5400
            octane_cam_tag[c4d.OCTANECAMERA_VIGNETTING] = 0
            octane_cam_tag[c4d.OCT_CAMIMAGER_EN_DENOISER] = True

            c4d.EventAdd()

    """Gamma=2.2    Cam Type = Linear    Click = Cam    Ctrl+Click = Target Cam   AI Denoise is ON"""
    def OctaneCam():
        c4d.CallCommand(1033865)  # Octane Camera
    """Normal Cam"""


    ## --- Lights --- ##

    #Octane Area light
    def OctaneAreaLight():
        c4d.CallCommand(1033864) # Octane Arealight
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "Area Light")
        c4d.EventAdd()


    #Octane Targeted Aera light
    def OctaneTargetAeraLight():
        c4d.CallCommand(1033868)
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "Target Light")
        c4d.EventAdd()


    ## --- Materials --- ##

    #Octane Diffuse
    def MatDiffuse():

        c4d.CallCommand(1033871, 1033871)
        obj = doc.GetActiveMaterial()
        obj.SetName("Diffuse")
        c4d.EventAdd()


    #Octane Glossy
    def MatGlossy():

        c4d.CallCommand(1033893, 1033893)
        obj = doc.GetActiveMaterial()
        obj.SetName("Glossy")
        c4d.EventAdd()


    #Octane Specular
    def MatSpecular():

        c4d.CallCommand(1033894, 1033894)
        obj = doc.GetActiveMaterial()
        obj.SetName("Specular")
        c4d.EventAdd()

    #Octane Mix
    def MatMix():

        c4d.CallCommand(1033895, 1033895)
        obj = doc.GetActiveMaterial()
        obj.SetName("Mix")
        c4d.EventAdd()

    #Convert Materials
    def ConvertMats():

        active_mat = doc.GetActiveMaterial()
        if active_mat == None:
            gui.MessageDialog("Please select at least one Material")

        c4d.CallCommand(1029770, 1029770)
        c4d.EventAdd()

    # Octane Blend
    def MatBlend():

        c4d.CallCommand(1040118)
        obj = doc.GetActiveMaterial()
        obj.SetName("Blend")
        c4d.EventAdd()

    # Octane Universal
    def MatUniversal():

        c4d.CallCommand(1041569)
        obj = doc.GetActiveMaterial()
        obj.SetName("Universal")
        c4d.EventAdd()

    # Octane Metallic
    def MatMetallic():

        c4d.CallCommand(1040116)
        obj = doc.GetActiveMaterial()
        obj.SetName("Metallic")
        c4d.EventAdd()

    # Octane Toon
    def MatToon():

        c4d.CallCommand(1040117)
        obj = doc.GetActiveMaterial()
        obj.SetName("Toon")
        c4d.EventAdd()





    ## --- Environments --- ##

    #HDRI Environment
    def HDRIEnv():

        c4d.CallCommand(1033867)
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "HDRI Environment")
        c4d.EventAdd()


    #Texture Environment
    def TextureEnv():

        c4d.CallCommand(1033866)
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "Texture Environment")
        c4d.EventAdd()



    ## --- Generators --- ##

    #Octane Scatter
    def OctaneScatter():

        c4d.CallCommand(1035961)
        c4d.EventAdd()


    #Octane Fog
    def OctaneFog():

        c4d.CallCommand(1036589, 1036589)
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "Fog")
        c4d.EventAdd()


    #Octane VDB
    def OctaneVDB():

        c4d.CallCommand(1037329, 1037329)
        obj = doc.GetActiveObject()
        obj.SetName(prefix + "VDB")
        c4d.EventAdd()



    ## --- Helpers --- ##

    #Octane Tex Manager
    def OctTexManager():

        c4d.CallCommand(1035275)
        c4d.EventAdd()


    #Octane Node Editor
    def OctNodeEditor():

        c4d.CallCommand(1033872)
        c4d.EventAdd()


    #Octane LiveDB
    def OctLiveDB():

        c4d.CallCommand(1033870)
        c4d.EventAdd()



    #Octane Live Viewer
    def LiveViewer():
        c4d.CallCommand(1029499)  # Live Viewer Window


    #Octane Setiing
    def Setting():
        if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.BFM_INPUT_CHANNEL, bc):

            if bc[c4d.BFM_INPUT_QUALIFIER] ==0:
                c4d.CallCommand(1031195)  # Octane Settings
                c4d.EventAdd()

            elif bc[c4d.BFM_INPUT_QUALIFIER] ==2 :
                c4d.CallCommand(1031195)  # Octane Settings
                rdata = doc.GetActiveRenderData()
                rdata[c4d.RDATA_RENDERENGINE] = 1029525
                OctaneRender = 1029525

                videopost = rdata.GetFirstVideoPost()

    """Click = Setting     Ctrl+Click = Setting & Set Renderer to Octane"""

    #Set Render Engine

    def OctaneRenderer():
        rdata = doc.GetActiveRenderData()
        rdata[c4d.RDATA_RENDERENGINE] = 1029525
        OctaneRender = 1029525

        videopost = rdata.GetFirstVideoPost()

    """Set Render Engine as Octane Renderer Open Octane Setting"""


    ########### -- User Input -- ###########

    result = gui.ShowPopupDialog(cd=None, bc=entries, x=c4d.MOUSEPOS, y=c4d.MOUSEPOS, flags = c4d.POPUP_RIGHT)

    if result == 10:
        LiveViewer()
    elif result == 11:
        OctNodeEditor()
    elif result == 12:
        Setting()

    elif result == 101:
        AIOctaneCam()

    elif result == 102:
        OctaneCam()

    elif result == 201:
        OctaneAreaLight()
    elif result == 202:
        OctaneDayLight()
    elif result == 203:
        OctaneTargetAeraLight()

    elif result == 301:
        HDRIEnv()
    elif result == 302:
        TextureEnv()

    elif result == 401:
        MatDiffuse()
    elif result == 402:
        MatGlossy()
    elif result == 403:
        MatSpecular()
    elif result == 404:
        MatMix()
    elif result == 405:
        ConvertMats()
    elif result == 406:
        MatUniversal()
    elif result == 407:
        MatMetallic()
    elif result == 408:
        MatBlend()
    elif result == 409:
        MatToon()





    elif result == 501:
        OctaneScatter()
    elif result == 502:
        OctaneFog()
    elif result == 503:
        OctaneVDB()

    elif result == 601:
        OctTexManager()
    elif result == 603:
        OctLiveDB()

    else:
        return


if __name__=='__main__':
    main()