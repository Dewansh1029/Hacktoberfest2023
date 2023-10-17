def check_module_online (device_handle, module_nu, sleep_time = 600):
    cmd_line = 'show module ' + str(module_nu)
    i = 1 
    module_ok = 0
    sleep_for = 1
    sleep_time += 60
    while sleep_for < sleep_time:
      try:
        oput = device_handle.execute(cmd_line)
      except:
        time.sleep(5)
        oput = device_handle.execute(cmd_line)
      lines = oput.splitlines() 
      module_pres = 0
      module_ok = 0
      j = 0
      for line in lines:
        j += 1
        if re.search('Module-Type', line, re.I):
           module_pres = 1
           break
      if not module_pres:
         log.info('Module %r is not Listed for device %r', module_nu,device_handle.name) 
         return 0
      j += 1
      line = lines[j]
      if re.search('active|ok|standby', line, re.I):
         return 1
      log.info('Sleeping for 60 seconds')
      time.sleep(60)
      sleep_for += 60 
      
    if not module_ok:
       log.info('Module %r is not online for device %r after %r seconds', module_nu,device_handle.name, sleep_time)
       return 0
    return 1
