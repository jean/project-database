#         
#Project Title (last value)              
#GEF Allocation (total of all Porjectstages)
#Cofinancing Cash (total of all Porjectstages)
#Cofinancing in Kind (total of all Porjectstages)
#Total Costs (total of all Porjectstages)
#Executing Agency (lead executing agency last value)
#Project Status (last value)
#expected Completion date (last value)
#revised completion date (last value)
##parameters=path=None
path=None

#results = container.portal_catalog(portal_type = 'Financials', sort_on='getStartDate', sort_order='reverse', review_state=['published','visible'],path=path)
results = container.portal_catalog(portal_type = 'Financials', review_state=['published','visible'])



resultdict = {}

i = 0
if results:
    lastResult = results[0].getObject()
    resultdict['Project Title'] = lastResult.title
    try:
        resultdict['Executing Agency']  = lastResult.getLeadExecutingAgency().title 
    except:
        resultdict['Executing Agency']  = ''
 
    resultdict['Project Status'] = lastResult.getStatus()
    resultdict['expected completion date'] = lastResult.getInitialCompletionDate()
    resultdict['revised completion date'] = lastResult.getRevisedCompletionDate()
    cofin_cash =0.0
    cofin_in_kind = 0.0
    gef_alloc = 0.0
        
    for resultitem in results:
        ro = resultitem.getObject()
        i +=1
        try:
            gef_alloc += 0 # float(ro.gef_trust_fund)
        except:
            pass
        try:
            gef_alloc += 0 # float(ro.ldc_fund_allocation)
        except:
            pass
        try:
            gef_alloc += 0 #float(ro.sccf_allocation)
        except:
            pass
        try:
            gef_alloc += 0 #float(ro.strategic_partnership)
        except:
            pass
        try:
            gef_alloc += 0 #float(ro.adaptation_trust_fund)
        except:
            pass  

        try:
            gef_alloc += float(ro.gef_project_allocation)
        except:
            pass

        cofin_vals = ro.getCofinancingCash()
        for cofin_val in cofin_vals:
            try:
                cofin_cash += float(cofin_val['cofinancing_cash_actual_amount'])    
            except:
                pass

        cofin_vals = ro.getCofinancingInKind()
        for cofin_val in cofin_vals:
            try:
                cofin_in_kind +=  float(cofin_val['cofinancing_inkind_actual_amount']) 
            except:
                pass

    resultdict['Total Costs']= cofin_in_kind + cofin_cash
    resultdict['Cofinancing Cash']= cofin_cash
    resultdict['Cofinancing in Kind']= cofin_in_kind 
    resultdict['GEF Allocation'] = gef_alloc
else:
    resultdict['Total Costs']= 0
    resultdict['Cofinancing Cash']= 0
    resultdict['Cofinancing in Kind']= 0
    resultdict['GEF Allocation'] = 0
    resultdict['Project Title'] = '' #lastResult.title
    resultdict['Executing Agency']  = '' #lastResult.getLead_executing_agency().getContentObject().title
    resultdict['Project Status'] = ''#lastResult.status
    resultdict['expected completion date'] = '' #lastResult.initial_completion_date
    resultdict['revised completion date'] = '' #lastResult.revised_completion_date
resultdict['i'] = i
return resultdict
