import html_creator as hc
import xml_creator as xc
import data_provider as dp

xc.new_create(dp.data_collection())
hc.new_create(dp.data_collection())
xc.create()
hc.create()
