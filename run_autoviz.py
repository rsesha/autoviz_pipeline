from matplotlib import pyplot as plt
import orchest

av_type = orchest.get_step_param('av_type')
chart_format = orchest.get_step_param("chart_format")
verbose = orchest.get_step_param("verbose")
print(av_type, chart_format, verbose)

from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

# Retrieve the data from the previous step.
data = orchest.get_inputs()
train, test, target = data["split_data"]

targetvar = target[0]

if av_type == 'train':
    ### we need to get inputs such as chart_format, verbose in order to run it ####
    _dft = AV.AutoViz(filename="", sep=',', depVar=targetvar, dfte=train, header=0, verbose=verbose, lowess=False,
               chart_format=chart_format,max_rows_analyzed=150000,max_cols_analyzed=30, save_plot_dir=None)
else:
    ### we need to get inputs such as chart_format, verbose in order to run it ####
    _dft = AV.AutoViz(filename="", sep=',', depVar=targetvar, dfte=test, header=0, verbose=verbose, lowess=False,
               chart_format=chart_format,max_rows_analyzed=150000,max_cols_analyzed=30, save_plot_dir=None)