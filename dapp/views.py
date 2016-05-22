from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from thirdparty import test

from thirdparty.temoa.db_io import Make_Graphviz
from thirdparty.temoa.temoa_model import temoa_model

import os

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def inputData(request):
    return render_to_response('InputData.html', context_instance=RequestContext(request))

def outputData(request):
    return render_to_response('OutputData.html', context_instance=RequestContext(request))

def modelRun(request):
    return render_to_response('ModelRun.html', context_instance=RequestContext(request))

def runModel(request):
  
  temoa_model.runModel()
  
  return HttpResponse("Generating model...")

def index(request):
  
  
  return HttpResponse("Nothing for now...")
  
  

# Create your views here.
def makeGraph(request):
  print test.tryme()
  
  #So we have to pass inputs to Make_Graphviz to generate graph
  #After getting response run a ajax call to get that
  
  filename = "/home/yash/Projects/dapp/thirdparty/temoa/db_io/temoa_utopia.sqlite"
  
  inputs = { 
            "-i" : filename , 
            "-f" : "svg",
            "--scenario" : "sname" ,
            "-o" : "result"
          }
  
  Make_Graphviz.createGraphBasedOnInput(inputs)
  
  
  #expected result
  # image svg now fetch and show result
  #print "result/%s/" %( os.path.splitext(os.path.basename(filename))[0] )
  
  
  
  
  #if opt in ("-i", "input"):
    #ifile = arg
  #elif opt in ("-f", "--format"):
    #graph_format = arg
  #elif opt in ("-c", "--show_capacity"):
    #show_capacity = True
  #elif opt in ("-v", "--splinevar") :
    #splinevar = True
  #elif opt in ("-t", "--graph_type") :
    #graph_type = arg
  #elif opt in ("-s", "--scenario") :
    #scenario = arg
  #elif opt in ("-n", "--name") :
    #quick_name = arg
  #elif opt in ("-o", "--output") :
    #res_dir = arg
  #elif opt in ("-g", "--grey") :
  
  
  
  return HttpResponse("Index SSS") 

