Search.setIndex({docnames:["backends","components","components/host","components/network","components/protocols","design","examples","examples/QKD","examples/chsh","examples/entanglement_routing","examples/packet_sniffing","examples/quantum_money","examples/send_data","examples/send_epr","index","install","install/linux_mac","install/windows","intro","objects","objects/classical_storage","objects/message","objects/packet","objects/quantum_storage","objects/qubit","objects/routing_packet","quick_start"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,sphinx:56},filenames:["backends.rst","components.rst","components/host.rst","components/network.rst","components/protocols.rst","design.rst","examples.rst","examples/QKD.rst","examples/chsh.rst","examples/entanglement_routing.rst","examples/packet_sniffing.rst","examples/quantum_money.rst","examples/send_data.rst","examples/send_epr.rst","index.rst","install.rst","install/linux_mac.rst","install/windows.rst","intro.rst","objects.rst","objects/classical_storage.rst","objects/message.rst","objects/packet.rst","objects/quantum_storage.rst","objects/qubit.rst","objects/routing_packet.rst","quick_start.rst"],objects:{"components.host":{Host:[2,1,1,""],_get_qubit:[2,3,1,""]},"components.host.Host":{_get_message_w_seq_num:[2,2,1,""],_get_sequence_number:[2,2,1,""],_log_ack:[2,2,1,""],_process_packet:[2,2,1,""],_process_queue:[2,2,1,""],add_c_connection:[2,2,1,""],add_c_connections:[2,2,1,""],add_checksum:[2,2,1,""],add_connection:[2,2,1,""],add_connections:[2,2,1,""],add_data_qubit:[2,2,1,""],add_epr:[2,2,1,""],add_ghz_qubit:[2,2,1,""],add_q_connection:[2,2,1,""],add_q_connections:[2,2,1,""],await_ack:[2,2,1,""],await_remaining_acks:[2,2,1,""],change_epr_qubit_id:[2,2,1,""],classical:[2,2,1,""],classical_connections:[2,2,1,""],delay:[2,2,1,""],empty_classical:[2,2,1,""],get_classical:[2,2,1,""],get_connections:[2,2,1,""],get_data_qubit:[2,2,1,""],get_data_qubits:[2,2,1,""],get_epr:[2,2,1,""],get_epr_pairs:[2,2,1,""],get_ghz:[2,2,1,""],get_next_classical_message:[2,2,1,""],get_sequence_number:[2,2,1,""],host_id:[2,2,1,""],is_idle:[2,2,1,""],max_ack_wait:[2,2,1,""],quantum_connections:[2,2,1,""],quantum_relay_sniffing_function:[2,2,1,""],rec_packet:[2,2,1,""],remove_c_connection:[2,2,1,""],remove_connection:[2,2,1,""],run_protocol:[2,2,1,""],send_ack:[2,2,1,""],send_broadcast:[2,2,1,""],send_classical:[2,2,1,""],send_epr:[2,2,1,""],send_ghz:[2,2,1,""],send_key:[2,2,1,""],send_qubit:[2,2,1,""],send_superdense:[2,2,1,""],send_teleport:[2,2,1,""],set_data_qubit_memory_limit:[2,2,1,""],set_epr_memory_limit:[2,2,1,""],set_quantum_relay_sniffing_function:[2,2,1,""],set_relay_sniffing_function:[2,2,1,""],shares_epr:[2,2,1,""],sniff_full_packet:[2,2,1,""],start:[2,2,1,""],stop:[2,2,1,""],storage_epr_limit:[2,2,1,""],storage_limit:[2,2,1,""]},"components.network":{Network:[3,1,1,""]},"components.network.Network":{_encode:[3,2,1,""],_entanglement_swap:[3,2,1,""],_process_queue:[3,2,1,""],_remove_network_node:[3,2,1,""],_route_quantum_info:[3,2,1,""],_update_network_graph:[3,2,1,""],add_host:[3,2,1,""],add_hosts:[3,2,1,""],classical_routing_algo:[3,2,1,""],delay:[3,2,1,""],draw_classical_network:[3,2,1,""],draw_quantum_network:[3,2,1,""],get_ARP:[3,2,1,""],get_classical_route:[3,2,1,""],get_host:[3,2,1,""],get_host_name:[3,2,1,""],get_quantum_route:[3,2,1,""],packet_drop_rate:[3,2,1,""],quantum_routing_algo:[3,2,1,""],remove_host:[3,2,1,""],send:[3,2,1,""],shares_epr:[3,2,1,""],start:[3,2,1,""],stop:[3,2,1,""],update_host:[3,2,1,""],use_hop_by_hop:[3,2,1,""],x_error_rate:[3,2,1,""],z_error_rate:[3,2,1,""]},"components.protocols":{_decode_superdense:[4,3,1,""],_encode_superdense:[4,3,1,""],_rec_classical:[4,3,1,""],_rec_epr:[4,3,1,""],_rec_ghz:[4,3,1,""],_rec_qubit:[4,3,1,""],_rec_superdense:[4,3,1,""],_rec_teleport:[4,3,1,""],_relay_message:[4,3,1,""],_send_ack:[4,3,1,""],_send_classical:[4,3,1,""],_send_epr:[4,3,1,""],_send_ghz:[4,3,1,""],_send_qubit:[4,3,1,""],_send_superdense:[4,3,1,""],_send_teleport:[4,3,1,""],encode:[4,3,1,""],process:[4,3,1,""]},"objects.classical_storage":{ClassicalStorage:[20,1,1,""]},"objects.classical_storage.ClassicalStorage":{add_msg_to_storage:[20,2,1,""],get_all:[20,2,1,""],get_all_from_sender:[20,2,1,""],get_next_from_sender:[20,2,1,""],remove_all_ack:[20,2,1,""]},"objects.message":{Message:[21,1,1,""]},"objects.message.Message":{content:[21,2,1,""],sender:[21,2,1,""],seq_num:[21,2,1,""]},"objects.packet":{Packet:[22,1,1,""]},"objects.packet.Packet":{await_ack:[22,2,1,""],payload:[22,2,1,""],payload_type:[22,2,1,""],protocol:[22,2,1,""],receiver:[22,2,1,""],sender:[22,2,1,""],seq_num:[22,2,1,""]},"objects.quantum_storage":{QuantumStorage:[23,1,1,""]},"objects.quantum_storage.QuantumStorage":{_check_memory_limits:[23,2,1,""],_check_qubit_in_system:[23,2,1,""],_decrease_qubit_counter:[23,2,1,""],_increase_qubit_counter:[23,2,1,""],add_qubit_from_host:[23,2,1,""],change_qubit_id:[23,2,1,""],check_qubit_from_host_exists:[23,2,1,""],get_all_qubits_from_host:[23,2,1,""],get_qubit_from_host:[23,2,1,""],release_storage:[23,2,1,""],set_storage_limit:[23,2,1,""]},"objects.qubit":{Qubit:[24,1,1,""]},"objects.qubit.Qubit":{H:[24,2,1,""],I:[24,2,1,""],K:[24,2,1,""],T:[24,2,1,""],X:[24,2,1,""],Y:[24,2,1,""],Z:[24,2,1,""],blocked:[24,2,1,""],cnot:[24,2,1,""],cphase:[24,2,1,""],host:[24,2,1,""],id:[24,2,1,""],measure:[24,2,1,""],qubit:[24,2,1,""],release:[24,2,1,""],rx:[24,2,1,""],ry:[24,2,1,""],rz:[24,2,1,""],send_to:[24,2,1,""],set_blocked_state:[24,2,1,""],set_new_host:[24,2,1,""],set_new_id:[24,2,1,""],set_new_qubit:[24,2,1,""]},"objects.routing_packet":{RoutingPacket:[25,1,1,""]},"objects.routing_packet.RoutingPacket":{decrease_ttl:[25,2,1,""],payload:[25,2,1,""],payload_type:[25,2,1,""],protocol:[25,2,1,""],receiver:[25,2,1,""],route:[25,2,1,""],sender:[25,2,1,""],ttl:[25,2,1,""]},components:{host:[2,0,0,"-"],network:[3,0,0,"-"],protocols:[4,0,0,"-"]},objects:{classical_storage:[20,0,0,"-"],message:[21,0,0,"-"],packet:[22,0,0,"-"],quantum_storage:[23,0,0,"-"],qubit:[24,0,0,"-"],routing_packet:[25,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function"},terms:{"boolean":[2,3,12],"break":11,"case":[2,8,15,16,17,23],"char":7,"class":[0,2,3,20,21,22,23,24,25],"default":[0,3,26],"export":[15,16],"final":[7,26],"float":[2,3,24],"function":[0,2,3,4,7,9,11,18,23,26],"import":[0,3,7,8,10,11,12,13,26],"int":[2,3,4,7,8,21,22,23,24,25],"long":[2,8],"new":[2,15,17,18,23,24,26],"return":[0,2,3,4,7,9,11,12,18,20,21,22,23,24,25],"true":[2,3,7,8,9,10,11,12,13,20,23,24,26],"try":9,"while":[7,9,11],AES:7,Eve:[0,7,10,11,12],For:[2,8,10,15,16,18,26],IDs:[0,2,7,25],Not:19,One:[2,4,8,18,26],The:[0,1,2,3,4,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26],Then:8,There:0,These:[11,23],With:[0,3,8,12],__main__:[7,8,10,11,12,13,26],__name__:[7,8,10,11,12,13,26],_check_memory_limit:23,_check_qubit_in_system:23,_decode_superdens:4,_decrease_qubit_count:23,_encod:3,_encode_superdens:4,_entanglement_swap:3,_get_message_w_seq_num:2,_get_qubit:2,_get_sequence_numb:2,_host:0,_increase_qubit_count:23,_log_ack:2,_process_packet:2,_process_queu:[2,3],_rec_class:4,_rec_epr:4,_rec_ghz:4,_rec_qubit:4,_rec_superdens:4,_rec_teleport:4,_relay_messag:4,_remove_network_nod:3,_route_quantum_info:3,_send_ack:4,_send_class:4,_send_epr:4,_send_ghz:4,_send_qubit:4,_send_superdens:4,_send_teleport:4,_update_network_graph:3,abil:[3,19],abl:7,about:18,abov:[15,16,17],access:[0,1,8,12,18,19],accomplish:2,accord:4,accur:18,achiev:[11,18],ack:[2,4,7,12,13,20,22],ack_arriv:[12,13],acknowledg:[2,4,12,18,21,26],acknowleg:2,act:[2,11],action:7,activ:[15,16,17],add:[0,2,3,7,9,10,12,15,17,19,20,23,24],add_c_connect:[2,8,13],add_checksum:2,add_connect:[0,2,7,8,9,10,11,12,13,26],add_data_qubit:2,add_edg:9,add_epr:2,add_ghz_qubit:2,add_host:[0,3,7,8,9,10,11,12,13,26],add_msg_to_storag:20,add_q_connect:[2,13],add_qubit_from_host:23,added:[2,3,12,13,18,23,26],adding:13,addit:24,address:21,advanc:[15,17],after:[9,11,12,15,16,17,23,25,26],again:[7,15,16,17],ahead:1,aim:11,algorithm:[3,7,9,18],alic:[0,7,8,10,12,26],alice_class:8,alice_func:7,alice_host:8,alice_id:8,alice_messag:10,alice_qkd:7,alice_quantum:8,alice_respons:8,alice_send_messag:7,all:[0,2,3,4,7,8,10,12,13,18,19,20,23,26],allow:[9,18],along:[11,22,26],alreadi:[2,15,17,18,23],also:[0,1,2,7,10,11,18,19,21],altern:[15,16,17],although:18,alwai:[0,10,13],amongst:8,amount:[2,3,9,18,23],amount_to_transmit:10,amount_transmit:10,analog:[2,22,25],angl:24,ani:[0,2,8,9,12,26],anoth:[0,2,3,4,8,18,23,24,26],answer:7,anymor:23,appear:21,append:[7,11],appli:[2,3,4,7,10,12,24,26],applic:[1,2,13,18],approach:8,arbitrari:[18,26],architectur:18,area:[15,17],arg:[2,4,8,9,11,13],argument:[0,2],around:18,arp:3,arrai:2,arriv:[2,12,13,18],assign:11,associ:11,assum:[12,26],assumpt:18,asynchron:18,attack:[6,14],attempt:11,avoid:18,awai:12,await:[2,4,8,11,12],await_ack:[2,4,7,8,9,10,11,12,13,22,26],await_remaining_ack:2,axi:8,back:[8,13],backend:[2,3,5,8,11,14,19,24],bad:7,bank:11,bank_basi:11,bank_bit:11,banker:11,banker_protocol:11,banknot:11,base:[2,3,7,9,11,18,20,21,22,23,24,25],basi:[7,8],basic:0,becaus:[7,8,12,23],becom:0,bee:7,been:[0,2,23],befor:[2,8,12],begin:[3,26],behav:2,being:[3,7,10,11,12,18,26],belong:[0,2,24],below:[0,7,8,9,10,11,12,13,15,18,19,22,26],best:9,better:[19,23,24],between:[3,10,18],bin:[15,16],binari:2,bit:[2,4,7,8],bit_no:11,block:[2,3,8,12,18,24,26],blown:18,bob:[0,7,8,10,12],bob_class:8,bob_host:8,bob_id:8,bob_quantum:8,bob_respons:8,bob_sniffing_class:10,bob_sniffing_quantum:10,bock:24,bool:[2,3,4,20,22,24],both:[8,18,23,26],bottom:[15,17],box:0,broadcast:2,buffer:[0,2],build:[3,9,13],built:[18,26],call:[0,2,8,12,23,26],came:13,can:[0,1,2,3,7,8,10,11,12,15,16,17,18,19,23,24,26],cannot:8,categor:19,caus:11,certain:1,chain:3,chang:[0,2,3,7,8,10,15,16,17,23],change_epr_qubit_id:2,change_qubit_id:23,channel:[2,6,14],cheat:11,cheat_alert:11,check:[2,7,11,23],check_qubit_from_host_exist:23,checksum:2,choic:[8,9],choos:[7,18],chose:0,chr:7,chsh:[6,14],clasic:2,classic:[2,3,4,5,7,8,10,11,12,13,18,19,21,22,25,26],classical_connect:2,classical_routing_algo:3,classical_storag:20,classicalstorag:20,clear:2,click:[15,17],clone:[15,16,17],cnot:24,code:[0,2,10,12,13,18,26],colour:18,com:[15,16,17],come:[1,18,23],comma:26,command:[15,16,26],common:[15,16,17,18],commonli:[2,3],commun:[7,8,12,18],compar:7,compil:[15,16,17],complet:26,complic:18,compon:[2,3,4,5,7,8,10,11,12,13,14,19,20,22,23,26],comput:[0,9],concaten:7,concatent:7,configur:[2,3,9,12,26],connect:[2,3,7,8,9,12,13,18,26],consid:[9,18],consist:4,consol:26,constant:22,constantli:9,contain:[4,10,21],content:[8,10,11,14,21,26],continu:[7,12],control:[3,11,24],cooper:8,core:18,correct:[11,15,16,17,18,26],correspond:2,could:[18,23],counter:23,cphase:24,cppsimul:[15,16,17],creat:[0,2,3,7,11,12,18,19,21,22],create_epr:0,create_qubit:0,creativ:26,crypto:7,current:[0,18,19],custom:[2,9,11,18],customer_protocol:11,daemonthread:2,data:[2,4,6,11,14,23,25],databas:11,dean:12,decid:7,decod:[1,4,7],decoher:19,decreas:[23,25],decrease_ttl:25,decrypt:7,decrypted_msg_from_alic:7,def:[0,7,8,9,10,11,12,13,26],defin:[0,3,7,10,13,24,26],delai:[2,3,7,8,10,11,12],delet:20,delt:20,demonstr:18,depend:[2,3,4,8,23,24],depict:3,describ:0,design:[14,18,19,26],dest:3,destin:[3,18],destruct:[0,11],detail:[18,19],determin:24,develop:[0,2,8,18,19,26],devis:8,di_graph:9,dict:[2,3,4],dictionari:[0,2,4],did:[12,13],didn:12,differ:[0,3,7,11,18,24,25],digraph:9,direct:[9,11,12,13],direction:[12,13],directli:[1,12,19,22],directori:[15,16,17],disabl:[7,8,10,11,13,26],distant:1,distantli:18,distribut:[2,3,4,6,8,11,14,18],disturb:[7,11],document:[15,16,17],doe:[2,4,8,11,19,23],doesn:[2,11],done:[8,9,13],dont:[15,16,17],dose:0,download:[15,16,17],draw:3,draw_classical_network:3,draw_quantum_network:3,driven:18,drop:3,dure:8,each:[1,3,7,8,9,12,15,23],eavesdrop:[2,6,14],eavesdropp:[2,10,11],edg:9,edit:[15,16,17],educ:18,either:[2,7,8,12,18],element:[2,26],elimin:[24,25],els:[2,7,8,9,12,13],empti:2,empty_class:2,empyt:20,encod:[1,2,3,4,22],encrypt:7,encrypted_msg_from_alic:7,encrypted_msg_to_ev:7,encrypted_text:7,end:[7,12,13],ensur:[8,12,26],entangl:[0,1,2,3,4,6,8,14,18],entanglement_network:9,enter:26,entir:2,environ:[15,16,17],epr:[2,3,4,6,8,14,18,23],epr_id:13,eqsn:[0,8],eqsn_backend:0,eqsnbackend:0,equat:8,error:[3,9],esqn:8,establish:[2,13,26],etc:22,eve:[7,10],eve_func:7,eve_kei:7,eve_qkd:7,eve_receive_messag:7,even:18,event:18,everi:11,exact:[8,23],exactli:9,exampl:[0,2,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,26],exceed:12,except:[8,9],excit:[10,12],exist:[2,15,17,18,20,23],exit:10,expect:0,expir:13,explanatori:0,explicitli:0,extern:4,extra:21,fals:[2,3,4,7,9,11,20,22,23,24],familiar:7,featur:[1,2,18],field:0,figur:13,file:[0,15,16,17,26],first:[2,7,10,11,12,13,26],flag:[3,12],flexibl:18,flow:[12,13],follow:[0,1,8,9,10,26],form:[4,13],format:8,found:18,framework:18,free:2,from:[0,2,3,4,7,8,9,10,11,12,13,18,20,23,24,25,26],from_host_id:[0,23],from_send:20,full:[7,8,9,10,11,12,13,18,26],fulli:26,func:2,further:19,futur:18,game:[6,14],gate:[0,3,12,24,26],gener:[1,2,3,7,8,9,13,15,16,17,18,19,22,26],generate_entangl:9,generate_epr_if_non:2,get:[2,3,4,7,11,12,15,16,17,18,20,23,26],get_al:20,get_all_from_send:20,get_all_qubits_from_host:23,get_apr:3,get_arp:3,get_class:[2,8,10,11],get_classical_rout:3,get_connect:[2,9],get_data_qubit:[2,7,10,11,12,26],get_epr:[2,8,13],get_epr_pair:[2,9],get_from_dict:0,get_ghz:2,get_host:[3,9],get_host_nam:3,get_inst:[0,7,8,9,10,11,12,13,26],get_next_classical_messag:[2,7],get_next_from_send:20,get_quantum_rout:3,get_qubit_from_host:23,get_sequence_numb:2,ghz:[2,4],git:[15,16,17],github:[15,16,17],give:[0,15,18,24,26],given:[3,20,23],global:[15,16,17],goe:25,got:13,graph:[3,9,18],greater:[3,15,16,17],grid:13,guid:14,hadamard:[24,26],half:[2,8],halv:2,handl:[2,18],happen:18,has:[0,1,2,3,7,8,9,11,12,23],have:[0,2,3,7,8,9,12,13,15,16,17,19,24,25,26],header:4,held:2,help:18,helper:7,her:[7,10,12],here:[1,7,8,10,12,13,15,16,17,26],high:18,him:10,his:[7,8,11],hop:[3,12,18,25],hope:19,hopefulli:0,host:[0,1,3,4,5,7,8,9,10,11,12,13,18,19,20,21,23,24,25,26],host_a:[8,13,26],host_alic:[0,7,10,12],host_b:[8,13,26],host_bank:11,host_bob:[0,7,10,12],host_c:[8,13,26],host_connect:9,host_custom:11,host_d:26,host_dean:12,host_ev:[0,7,10,11,12],host_id:[0,2,3,7,8,9,11,13,23,26],host_id_list:2,how:[0,2,7,8,9,10,11,13,15,16,17,18,19,26],howev:[0,7],ident:24,idl:[2,9],ids:2,imag:18,implement:[0,7,11,23,25],includ:[15,16,17,26],increas:23,inform:[0,1,2,3,4,11,12,13,18,24],initi:[0,7,8,10,11,18,26],inspir:18,instal:[8,14,16,17,26],instanc:0,instead:[0,8],instruct:[13,15,16,17,26],instructor:18,integr:19,intend:[2,4,18],inter:23,interact:[1,22],interfac:0,internet:[0,22,25],interv:3,introduct:14,invalid:11,invers:9,is_idl:[2,9],isinst:10,isn:20,issu:[15,16,17],item:26,iter:[7,18,19],its:[3,18],join:[7,10,11],just:[0,2,3,15,16,17,26],keep:2,kei:[1,2,6,14,18,19],key_arrai:7,key_array_to_key_str:7,key_siz:[2,7],key_string_binari:7,know:[2,7,10,11,18,24],knowledg:0,larg:9,last:2,later:11,layer:[1,3,18,22,25],learn:18,leav:26,len:9,length:[2,3],let:[7,9,10],level:[15,16,17,18],librari:[8,18],like:[2,18],limit:[2,23],line:[12,18],linear:12,link:[9,13],linux:14,list:[2,3,9,18,19,20,22,25,26],listen:[7,26],live:[3,25],local:2,locat:[15,16,17],lock:0,log:[2,8,18],logger:[7,8,9,10,11,13,26],logic:12,look:0,loser:8,lost:[8,12],lower:3,mac:[14,16],made:[19,23],mai:[15,16,17,18],main:[7,8,9,10,11,12,13,25,26],mainli:[18,24],maintain:3,make:[0,7,15,16,17,18,26],man:[6,14],manag:24,mani:[2,26],manipul:[2,10,19],map:0,match:[7,11],math:8,matplotlib:3,matter:8,max:23,max_ack_wait:[2,12],maximum:[2,12],mean:[12,18],measur:[4,7,8,10,11,12,13,24,26],measured_valu:24,measurement_bas:7,memori:[2,18,23],messag:[2,4,5,7,8,9,10,11,18,19,20],method:[0,2,3,8,13,18,26],middl:[6,14],might:0,mind:12,mismatch:11,mode:23,model:19,modifi:[4,10],modular:0,moment:[8,18],monei:[6,14],money_qubit:11,more:[0,8,18,23,26],most:[0,2,3,15,16,17],mostli:1,move:18,msg:[2,7,10],msg_buff:7,msg_to_ev:7,multi:18,multipl:0,must:[3,9],name:[3,8,15,16,17,26],neccessari:3,necessari:[0,1,2,7],need:[0,1,7,8,12,13,15,17,22,24,26],network:[0,2,4,5,7,8,9,10,11,12,13,18,25,26],networkx:[9,18],never:[1,19],new_host:0,new_id:[2,23,24],new_limit:23,newli:9,next:[2,4,7,8,10,12,20,23,26],no_of_seri:11,node:[0,2,3,4,7,8,9,10,11,12,13,18,26],node_1:9,node_2:9,nois:2,non:11,non_destruct:[11,24],none:[2,3,4,7,12,13,20,23,24],normal:26,note:[9,11,12,13,26],noth:9,now:[0,7,10,12,13],num_epr_pair:9,number:[0,2,3,4,8,11,18,21,22,25,26],numpi:[0,7],o_seq_num:3,object:[0,1,2,3,5,7,8,10,11,12,14,20,21,22,23,24,25,26],occur:23,offer:18,often:8,old:2,old_id:[2,23],onc:[0,2,3,7,18],one:[0,2,3,7,8,12,13,15,16,18,20,23,26],onli:[1,8,11,12,13,15,16,17,20,23,26],onward:18,open:[15,17,26],oper:[4,8,10,15,24],optic:8,option:[2,15,16,17,20,23],ord:7,order:[2,3,9,18],other:[0,2,7,8,12,13,22,23],otherwis:[2,3,7,15,17,23],our:[1,7,10,24,25],out:[0,11,18],outcom:24,outperform:8,output:10,over:[0,7,18],overview:[14,18,19,26],own:[3,4,5,7,12,14,18,24],owner:0,packag:[0,15,16,17],packet:[1,2,3,4,5,10,12,18,19,26],packet_drop_r:3,pair:[0,2,3,4,6,8,14,23],parallel:12,param:[2,3,4],paramet:[2,3,4,9,13,20,23,24,26],pars:4,part:[0,1,2,11,12,15,17],parti:[7,8,11,12,26],particular:2,partner:2,pass:[0,2],path:[3,9,15,16,17],path_to_qunetsim:[15,17],pauli:24,payload:[2,3,4,18,22,25],payload_typ:[3,4,22,25],per:2,perform:[1,3,8,10,15,16,17,24],phi:24,physic:[18,19,24],piec:19,pip:[15,16,17],place:12,plai:[3,8,11],plan:[19,23],player:8,plot:3,point:8,polar:11,popular:0,possess:11,possibl:[0,18],potenti:18,pre:7,prepar:[0,10,11],preparation_and_distribut:11,present:18,principl:26,print:[7,8,9,10,11,12,13,26],privat:1,probabl:[3,8],problem:7,procedur:[1,18],proceed:2,process:[2,3,4,9,18],processor:2,program:[1,10],programm:12,progress:18,project:[15,16,17],projectq:[0,8,15,16,17],projectq_backend:[8,11],projectqbackend:[8,11],prompt:26,properli:[13,15,16,17],properti:[2,3,15,17,21,22,24,25],protocol:[1,2,3,5,7,8,9,10,11,12,13,18,19,22,25,26],protocol_1:[13,26],protocol_2:[13,26],protocol_param:2,provid:[0,18],purpos:[2,23],put:[1,2,3,12,18],pwd:[15,16],python3:[15,16,17],python:[8,15,16,17,18,26],pythonpath:[15,16,17,26],q_bit:7,q_id:[2,3,12,13,23,24],q_rec:12,qkd:[2,7],quantum:[0,2,3,4,5,6,8,9,12,13,18,19,22,25,26],quantum_connect:2,quantum_relay_snif:[10,11],quantum_relay_sniffing_funct:2,quantum_routing_algo:[3,9],quantum_storag:23,quantumli:8,quantumstorag:23,qubit:[0,2,3,4,5,6,7,8,10,11,14,18,19,23,25,26],qubit_id:2,qubit_no:11,qubits_per_monei:11,queue:[2,3],quick:14,quit:19,qunetsim:[0,1,2,3,7,8,11,12,15,16,17,19,21,23,24,26],rad:24,ran:26,randint:[7,11],random:[2,7,8,9,11,23],random_bas:11,random_bit:11,randomli:7,rang:[8,9,10,11,12,13,26],rate:3,ratio:8,reach:23,read:[0,7],real:[0,7,18],realist:18,realiz:11,realli:7,rec_packet:2,recalcul:3,receiv:[2,3,4,7,8,9,10,11,13,22,23,25,26],receive_epr:0,receive_from_id:2,receive_monei:11,received_count:7,receiver_id:[2,24],receiver_list:2,recommend:[0,15],record:[8,11],recov:18,reduc:4,ref:8,refere:8,referee_id:8,referee_messag:8,regard:[2,18],rel:18,relai:[1,2,3,4,11,18,25],relay_snif:10,releas:[23,24],release_qubit:2,release_storag:23,remain:[2,26],remov:[2,3,8,15,16,17,20,23,25],remove_all_ack:20,remove_c_connect:2,remove_connect:[2,8],remove_host:3,repeat:7,replac:[15,17,19],repositori:[15,16,17],repres:[1,2,3,11,12,13,18,19],represent:[3,9],reproduc:11,request:22,requir:[4,15,16,17,18,26],res:8,resolv:[15,16,17],resourc:8,respect:8,respons:[0,1,8],result:[4,7,11,12,26],retriev:[2,4],right:[0,7],rise:0,robust:18,role:[1,3],rotat:[8,24],roughli:8,rout:[1,2,3,5,6,10,13,14,18,19],router:2,routing_algorithm:9,routing_packet:25,routingpacket:[3,4,25],run:[1,2,3,7,8,9,11,12,13,15,16,17,26],run_protocol:[2,7,8,9,10,11,13,26],rwlock:0,safe:[0,12,13],safedict:0,sai:12,same:[7,8,12,15,16,17,18,23,26],saw:10,script:[15,16,17,26],second:[0,2,9,13,26],secret:[2,7,18],secret_kei:7,secret_key_str:7,section:[0,2,18,19,26],secur:7,see:[0,2,7,8,9,10,11,12,13,15,16,17,18,19,26],seem:0,self:0,send:[2,3,4,6,7,8,9,10,11,14,18,21,24,26],send_ack:2,send_broadcast:2,send_class:[2,7,8,10,11],send_epr:[2,8,9,13],send_ghz:2,send_kei:2,send_qubit:[2,7,10,11,12,26],send_qubit_to:0,send_superdens:[2,9],send_teleport:2,send_to:24,sender:[2,3,4,7,9,10,11,13,20,21,22,25,26],sender_id:[2,20],sens:18,sent:[0,2,3,7,10,12],seq:2,seq_num:[2,8,10,11,21,22],seq_numb:[2,4],sequenc:[2,4,18,21,22],sequence_nr:[2,7],sequence_num:4,sequence_numb:[2,22],serial:11,serial_of_money_to_be_us:11,serial_to_be_check:11,set:[0,1,2,3,7,8,10,11,12,13,15,16,17,20,23,24,26],set_blocked_st:24,set_data_qubit_memory_limit:2,set_delai:9,set_epr_memory_limit:2,set_new_host:[0,24],set_new_id:24,set_new_qubit:24,set_quantum_relay_sniffing_funct:[2,10,11],set_relay_sniffing_funct:[2,10],set_storage_limit:23,share:[2,3,7,8,9],shares_epr:[2,3],she:[7,8,11,12],shortest:[3,9],shortest_path:9,should:[0,2,3,4,7,8,10,13,14,15,16,20,23,24,25,26],show:[8,13],shown:[0,11],side:12,signal:3,similar:[8,12],simpl:[13,18,26],simpli:[0,8,10,18],simul:[0,3,8,12,15,16,17,18,19,23],simulaqron:[0,8],simular:25,sinc:[15,16,17],singl:[0,26],singleton:3,sit:[10,12],size:[2,7],size_per_qubit:2,sleep:9,small:[7,15,16,17],snif:2,sniff:2,sniff_full_packet:2,sniffer:10,sniffing_quantum:11,snippet:0,softwar:0,solv:7,some:[0,9,11,18,21,25,26],someth:12,sometim:[3,18],sort:2,sourc:[3,9,15,16],specif:[0,2,8,18,23,26],specifi:[2,13],split:7,squar:13,stai:24,standard:[15,16,17],start:[0,2,3,7,8,9,10,11,12,13,14,15,16,17],state:[2,4,10,11,12,18,24,26],statist:8,statu:2,steal:11,step:[9,15,16,17,18,26],still:[7,18],stop:[0,2,3,9,10,11,12],stop_host:[3,9,12],storag:[2,4,5,19,21],storage_epr_limit:2,storage_limit:2,storage_limit_individually_per_host:23,store:[0,2,4,18,19,20,23],str:[2,3,4,7,8,9,11,12,13,21,22,23,24,25],strategi:8,string:[2,4,7,20,21,23,24],structur:[0,15,16,17,18,19,21],student:18,stuff:0,style:[3,12],superdens:[2,4,9,18],support:[4,8],sure:[15,16,17],swap:[3,18],system:[8,15,17,23,24],tabl:3,take:[3,25,26],talk:[7,11],target:[9,24],task:[0,18],team:0,teh:11,teleport:[2,4,18],tell:12,templat:[15,16,17,26],termin:[15,16,26],test:[7,9,18,26],text:7,than:[0,3,8,26],thei:[2,7,8,22,23,24,25],them:[2,7,8,10],themselv:8,therefor:[0,11,18,21],thi:[0,2,3,7,8,9,10,11,12,13,15,16,17,18,20,23,24,25,26],thing:18,those:[8,18],thread:[0,2,3,7,18],three:[0,7,8,9,11],throttl:3,through:[2,10,11,13,18],tick:2,till:0,time:[1,2,3,8,9,12,13,18,25],to_host_id:0,toi:18,too:[2,7],tool:[0,18],topolog:7,tqsd:[0,15,16,17],trace:18,traffic:[12,13],transfer:11,transmiss:[3,7,11],transmit:[0,4,12,18],transport:[1,18,22,25],travel:25,treat:18,trigger:[18,22],trivial:7,ttl:[3,4,25],tupl:[2,26],two:[0,1,2,3,7,8,12,18,23,26],txt:[15,16,17],type:[0,2,3,4,9,13,21,22,24,25,26],typic:18,unblock:2,underli:[19,24],undo:10,unforg:11,uni:[12,13],uniqu:24,unknown:18,unread:20,unrealist:18,until:[2,7,12,18],updat:3,update_host:[3,8],upgrad:[15,16,17],usabl:23,use:[2,7,8,11,12,13,14,15,16,17,19,26],use_hop_by_hop:[3,9],used:[0,1,2,3,7,19,20,23],user:[1,2,15,16,18,22],uses:[3,8,18],using:[0,7,8,9,11,12,13,15],valid:11,valu:[2,3,12,15,17],variabl:[0,3,15,17,26],variou:19,venv:[15,16,17],verifi:11,verify_monei:11,version:[1,15,16,17],vertic:9,via:[2,3,10,18],virtual:[15,16,17],wai:[7,11,12,18],wait:[2,7,8,10,11,12,13,26],wait_tim:[7,11],want:[7,10,11,18,26],warn:7,weight:9,weird:0,were:26,what:[4,7,8,11,12,14],when:[1,3,8,9,13,18,21,25],where:[8,12,13,15,16,17,19],whether:[2,3],which:[0,2,3,4,7,10,15,16,17,18,23,24,25],who:[2,10,11,12,14,20,23,24],whole:2,whom:[2,23],whose:3,wiesner:11,win:8,window:14,winner:8,without:[7,12,15,16,17],won:8,word:19,work:[0,7,9,18,26],would:[0,26],wrapper:24,write:[1,5,12,13,14,18,26],x_error_r:3,xor:8,yet:7,you:[0,7,15,16,17,26],your:[5,14,15,16,17,26],z_error_r:3,zip:7},titles:["Backends","Network Components","Host","Network","Protocols","Design Overview","Examples","Quantum Key Distribution","CHSH Game","Routing with Entanglement","Eavesdropping on channels","Quantum Money with a Man-in-the-Middle Attack","Send Data Qubits","Send EPR Pairs","QuNetSim: A quantum network simulation framework","Install","&lt;no title&gt;","&lt;no title&gt;","Introduction","Network Objects","Classical Storage","Message","Packet","Quantum Storage","Qubit","Routing Packet","Quick Start Guide"],titleterms:{attack:11,backend:0,channel:10,chsh:8,classic:20,compon:1,data:12,design:5,distribut:7,eavesdrop:10,entangl:9,epr:13,exampl:6,framework:14,game:8,guid:26,host:2,instal:15,introduct:18,kei:7,linux:15,mac:15,man:11,messag:21,middl:11,monei:11,network:[1,3,14,19],object:19,overview:5,own:0,packet:[22,25],pair:13,protocol:4,quantum:[7,11,14,23],qubit:[12,24],quick:26,qunetsim:[14,18],rout:[9,25],send:[12,13],should:18,simul:14,start:26,storag:[20,23],use:18,what:18,who:18,window:15,write:0,your:0}})