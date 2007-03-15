"""
Configuration file.
Custom settings and variables to be used throughout this product.
"""

__author__ = "Millie Ngoka (miriam.ngoka@unep.org)"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "United Nations Environment Programme"
__license__ = "Python"

# Import permission for adding types
from Products.CMFCore.CMFCorePermissions import AddPortalContent

# Import 'DisplayList' function a data container for use when displaying pulldowns/radiobuttons
from Products.Archetypes.public import DisplayList

PROJECTNAME = "ProjectDatabase"
SKINS_DIR = 'skins'
GLOBALS = globals()
PROJECTDATABASE_FOLDER_DATA = {'id': 'projectsdatabase', 'title': 'Projects Database'}

ADD_CONTENT_PERMISSION = AddPortalContent
EDIT_CONTENTS_PERMISSION = 'ProjectType: Edit'
# VIEW_CONTENTS_PERMISSION = 'ProjectType: View'

# List definitions

FOCAL_AREAS = DisplayList((
    ('', 'Select One'),
    ('BD', 'Biodiversity'),
    ('CC', 'Climate Change'),
    ('IW', 'International Waters'),
    ('LD', 'Land Degradation'),
    ('PO', 'Persistent Organic Pollutants'),
    ('OD', 'Ozone Depletion'),
    ('MF', 'Multiple Focal Areas'),
    ))

OPERATIONAL_PROGRAMMES = DisplayList((
    ('1', 'OP1 - Arid and Semi-Arid Ecosystems'),
    ('2', 'OP2 - Costal Marine and Freshwater Ecosystems'),
    ('3', 'OP3 - Forest Ecosystems'),
    ('4', 'OP4 - Mountain Ecosystems'),
    ('BD-EA', 'EA - Biodiversity Enabling Activities'),
    ('BD-STRM', 'STRM - Biodiversity Short Term Measures'),
    ('5', 'OP5 - Removal of Barriers to Energy Efficiency and Energy Conservation'),
    ('6', 'OP6 - Promoting the Adoption of Renewable Energy by Removing Barriers and Reducing Implementation Costs'),
    ('7', 'OP7 - Reducing long term costs of low greenhouse gas-emitting energy technologies'),
    ('11', 'OP11 - Promoting Environmentally Sustainable Transport'),
    ('CC-EA', 'EA - Climate Change Enabling Activities'),
    ('CC-STRM', 'STRM - Climate Change Short Term Measures'),
    ('8', 'OP8 - Water based Program'),
    ('9', 'OP9 - Integrated Ecosystem and Resource Management'),
    ('10', 'OP10 - Contaminant-Based Program'),
    ('STRM', 'STRM - Projects and Country Programs to identify/prepare eligible projects.'),
    ('12', 'OP12 - Integrated Ecosystem Management'),
    ('MF-EA', 'EA - Multiple Focal Areas Enabling Activities'),
    ('MF-STRM', 'STRM - Multiple Focal Areas Short Term Measures'),
    ('IW-STRM', 'STRM - International Waters Short Term Measures'),
    ('IW-EA', 'EA - International Waters Enabling Activities'),
    ('LD-EA', 'EA - Land Degradation Enabling Activities'),
    ('OD-EA', 'EA - Ozone Depletion Enabling Activities'),
    ('PO-EA', 'EA - Persistent Organic Pollutants Enabling Activities'),
    ('PO-STRM', 'STRM - Persistent Organic Pollutants Enabling Activities'),
    ('OD-STRM', 'STRM - Ozone Depletion Short Term Measures'),
    ('13', 'OP13 - Conservation and Sustainable Use of Biological Diversity Important to Agriculture'),
    ('14', 'OP14 - Draft Operational Program on Persistent Organic Pollutants'),
    ('15', 'OP15 - Operational Program on Sustainable Land Management'), 
    ))


STRATEGIC_PRIORITIES = DisplayList((
    ('BD1', 'Catalyzing Sustainability of Protected Areas'),
    ('BD2', 'Mainstreaming Biodiversity in Production Landscapes and Sectors'),
    ('BD3', 'Capacity Building for the Implementation of the Cartagena Protocol on Biosafety'),
    ('BD4', 'Generation and Dissemination of Best Practices for Addressing Current and Emerging Biodiversity Issues'),
    ('CC1', 'Transformation of Markets for High Volume Products and Processes'),
    ('CC2', 'Increased Access to Local Sources of Financing for Renewable Energy and Energy Efficiency'),
    ('CC3', 'Power Sector Policy Frameworks Supportive of Renewable Energy and Energy Efficiency'),
    ('CC4', 'Productive Uses of Renewable Energy'),
    ('CC5', 'Global Market Aggregation and National Innovation for Emerging Technologies'),
    ('CC6', 'Modal Shifts in Urban Transport and Clean Vehicle/Fuel Technologies'), 
    ('CC7', 'Short Term Measures'),
    ('IW1', 'Catalyzing Financial Resources for Implementation of Agreed Actions'),
    ('IW2', 'Expand Global Coverage with Capacity Building Foundational Work'),
    ('IW3', 'Undertake Innovative Demonstrations for Reducing Contaminants and Addressing Water Scarcity'),
    ('OZ1', 'Methyl Bromide Reduction'),
    ('POP1', 'Targeted Capacity Building'),
    ('POP2', 'Implementation of Policy/Regulatory Reforms and Investments'),
    ('POP3', 'Demonstration of Innovative and Cost Effective Technologies'),
    ('SLM1', 'Targeted Capacity Building'),
    ('SLM2', 'Implementation of Innovative and Indigenous Sustainable Land Management Practices'),
    ('CB1', 'Enabling Activities'),
    ('CB2', 'Crosscutting Capacity Building'),
    ('EM1', 'Integrated Approach to Ecosystem Management'),
    ('SGP1', 'Small Grants Progam'),
    ))

PROJECT_TYPES = DisplayList((
    ('EA', 'EA'),
    ('FSP', 'FSP'),
    ('MSP', 'MSP'),
    ))



PIPELINE_NUMBERS = DisplayList((
    ('', 'Select One'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'), 
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),    
    ))
    
SCOPE = DisplayList((
    ('Global', 'Global'),
    ('Multi - Country', 'Multi - Country'),
    ('Regional Multi - Country', 'Regional Multi - Country'),
    ('Regional', 'Regional'),
    ('National', 'National'),
    ))
    

REGION = DisplayList((
    ('Africa', 'Africa'),
    ('Americas', 'Americas'),
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('Global', 'Global'),
    ('Oceania', 'Oceania'),
    ))
  
 
LEAD_AGENCY = DisplayList((
    ('', 'Select One'),
    ('AFDB', 'African Development Bank'),
    ('ADB', 'Asian Development Bank'),
    ('EBRD', 'European Bank for Reconstruction and Development'),
    ('FAO', 'Food and Agriculture Organization'),
    ('IADB', 'Inter-American Development Bank'),
    ('IFAD', 'International Fund for Agriculture and Development'),
    ('UNDP', 'United Nations Development Programme'),
    ('UNEP', 'United Nations Environment Programme'),
    ('IBRD', 'World Bank'),
    )) 
 
 
GEF_PHASE = DisplayList((
    ('', 'Select One'),
    ('Pilot', 'Pilot'),
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ))
  
  
STAGE = DisplayList((
    ('', 'Select One'),
    ('Concept', 'Concept'),
    ('Pipelined', 'Pipelined'),
    ('PDFA', 'PDFA'),
    ('PDFB', 'PDFB'),
    ('GEF Approved EA', 'GEF Approved EA'),
    ('MSP', 'MSP'),
    ('FSP', 'FSP'),
    ))


STATUS = DisplayList((
    ('', 'Select One'),
    ('Ongoing', 'Ongoing'),
    ('Inactive', 'Inactive'),
    ('Complete', 'Complete'),
    ('Closed', 'Closed'),
    ))
    

PROJECT_STATUS = DisplayList((
    ('', 'Select One'),
    ('Agency Concept', 'Agency Concept'),
    ('GEF Approved Concept', 'GEF Approved Concept'),
    ('GEF Approved Project', 'GEF Approved Project'),
    ('PDFA', 'PDFA'),
    ('PDFB', 'PDFB'),
    ('Under Implementation', 'Under Implementation'),
    ('Completed', 'Completed'),
    ('Closed', 'Closed'),
    ))
    

FINANCE_CATEGORY = DisplayList((
    ('', 'Select One'),
    ('EA', 'EA'),
    ('FSP', 'FSP'),
    ('MSP', 'MSP'),
    ('PDF A', 'PDF A'),
    ('PDF B', 'PDF B'),
    ))
    
DONOR_TYPE = DisplayList((
    ('', 'Select One'),
    ('Implementing Agency', 'Implementing Agency'),
    ('Executing Agency', 'Executing Agency'),
    ('Government', 'Government'),
    ('Multilateral', 'Multilateral'),
    ('Bilateral', 'Bilateral'),
    ('Private Sector', 'Private Sector'),
    ('NGO', 'NGO'),
    ('Communities', 'Communities'),
    ('Other', 'Other'),
    ))
    

MILESTONE_VALUES = DisplayList((
    ('Date of receipt of project concept', 'Date of receipt of project concept'),
    ('Date of review by Focal Area Task Force', 'Date of review by Focal Area Task Force'),
    ('Date of submission to DROC', 'Date of submission to DROC'),
    ('Date of submission to SMG', 'Date of submission to SMG/PCC'),
    ('Date of national GEF Focal Point endorsements', 'Date of national GEF Focal Point endorsements'),
    ('Date of submission to GEF', 'Date of submission to GEF'),
    ('GEF Secretariat Review Sheet', 'GEF Secretariat Review Sheet'),
    ('Pipeline Entry Date', 'Pipeline Entry Date'),       
    ('Resubmission to GEF', 'Resubmission to GEF'),
    ('Work Program Entry', 'Work Program Entry'),
    ('Circulation to Council', 'Circulation to Council'),
    ('CEO Approval', 'CEO Approval (PDF-B or MSP or EA)'),
    ('CEO Endorsement', 'CEO Endorsement (for FSP)'),    
    ('GEF Approval Date', 'GEF Approval Date'),
    ('Approval Date', 'UNEP Approval Date'),
    ('UNEP Approval date', 'UNEP Approval date'),
    ('Estimated Start Date', 'Estimated Start Date'),
    ('Actual Start Up date', 'Actual Start Up date'),
    ('Financial Closure Date', 'Financial Closure Date'),
    ))
    
STATUS_VALUES = DisplayList((
    ('Concept', 'Concept'),
    ('Pipelined', 'Pipelined'),
    ('PDFA', 'PDFA'),
    ('PDFB', 'PDFB'),
    ('EA', 'EA'),
    ('MSP', 'MSP'),
    ('FSP', 'FSP'),
    ))    
   

IMPLEMENTATION_TYPE = DisplayList((
    ('Internal', 'Internal'),
    ('External', 'External'),
    ))
    
REPORT_TYPE = DisplayList((
    ('Progress Report', 'Progress Report'),
    ('Expenditure Statements', 'Expenditure Statements'),
    ('Audit Report', 'Audit Report'),
    ('Co-finance', 'Co-finance'),
    ('Inventory', 'Inventory'),
    ('Final/Terminal Report', 'Final/Terminal Report'),
    ))
