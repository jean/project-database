def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('unep.theme_various.txt') is None:
        return

    # Add additional setup code here

def _setupSkins(context, skin_prefix, definition=None):
    """
    GS ignores the 'insert-after' directive in skins.xml and ArchgenXML does not provide
    for multiple skins in skins.xml.

    Parameter definition has form eg. 
        {'Plone Default':
            ['plone4radioblog_common','plone4radioblog_admin','plone4radioblog_admin_plone']}

    Parameter skin_prefix is eg. plone4radioblog.

    This function ensures that only desirable layers are present in the skin. It does not 
    add any new layers - that is handled by GS. It changes layers and their order.

    The layers are hard-coded to appear after custom.
    """
    portal = context.getSite()
    ps = portal.portal_skins
    skins = ps._getSelections()

    if definition is None:
        definition = _defaultSkinDefinition(skin_prefix)

    for skin, layers in definition.items():
        if not skin in skins: continue
        new_layers = []
        current_layers = skins[skin].split(',')
        for current_layer in current_layers:
            if current_layer.startswith(skin_prefix) and \
               (current_layer not in layers):
                # This layer must be removed from the skin
                pass
            else:
                new_layers.append(current_layer)

        # Change the layer order
        layers.reverse()
        for layer in layers:
            if layer in new_layers:
                new_layers.remove(layer)
                new_layers.insert(1, layer)
            else:
                new_layers.insert(1, layer)

        skins[skin] = ','.join(new_layers)

def changeSkinLayers(context):
    import pdb; pdb.set_trace()
    _setupSkins(context, 'projectdatabase')
    _setupSkins(context, 'unep_theme')
