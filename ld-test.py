import ldclient
from ldclient.config import Config

LD_SDK_KEY='<TODO: Insert LD SDK key here>'
FLAG_KEY='<TODO: Insert LD flag key here>'

ldclient.set_config(Config(LD_SDK_KEY))
ld_client = ldclient.get()

show_feature = ld_client.variation(FLAG_KEY, {"key": "user@test.com"}, False)
print(show_feature)

ldclient.get().flush()
#ldclient.get().close() # If you uncomment this LD updates the 'Evaluated ...' string correctly