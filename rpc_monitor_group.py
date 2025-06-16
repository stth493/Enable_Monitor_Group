


NETCONF_Get_description = '''
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
      <interface>
        <name>{{ INTERFACE }}</name>
          <subinterfaces>
          <subinterface>
            <index>{{ VLAN }}</index>
            <config>
            <description/>
            </config>
          </subinterface>
          </subinterfaces>
      </interface>
    </interfaces>

'''


NETCONF_Monitor_Group = '''
{% set WEIGHT = (100/(IP_PE_LIST | length))|int %}
<config>
<route-monitor-group xmlns="urn:huawei:yang:huawei-route-monitor-group">
  <monitor-groups>
    <monitor-group>
      <group-name>track_Uplink</group-name>
      <enable-status>true</enable-status>
      <trigger-up-delay>10</trigger-up-delay>
      <track-routes>
      
      {% for IP_PE in IP_PE_LIST %}
        <track-route>
        <destination-ni-name>_public_</destination-ni-name>
        <destination>{{ IP_PE }}</destination>
        <mask-length>32</mask-length>
        <down-weight>{{ WEIGHT }}</down-weight>
        </track-route>
      {% endfor %}
    
      </track-routes>
    </monitor-group>
  </monitor-groups>
</route-monitor-group>
</config>
'''


NETCONF_track_interface = '''
<config>
  <ifm xmlns="urn:huawei:yang:huawei-ifm">
    <interfaces>
    
      {% for INTERFACE in INTERFACE_LIST %}
      
      <interface>
      <name>{{ INTERFACE }}</name>
      <ipv4 xmlns="urn:huawei:yang:huawei-ip">
      <rgm xmlns="urn:huawei:yang:huawei-rgm">
      <track-rtmtg>
      <name>track_Uplink</name>
      <down-weight>100</down-weight>
      </track-rtmtg>
      </rgm>
      </ipv4>
      </interface>

      {% endfor %}
    
    </interfaces>
  </ifm>
</config>
'''