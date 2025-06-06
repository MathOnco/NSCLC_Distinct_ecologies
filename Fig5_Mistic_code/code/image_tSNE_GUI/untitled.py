#31st Jan 2022
###############
#uncomment for single montage
###############

### 14th feb 2022
# adding this to create_figure()

if (stack_montage_flag==True):
    '''
    commented on the 9th Feb 2022
    ### uncomment for tycif files
    ## need to update the markers_single array based on the order the files are read in 
    ms_list=[]
    cluster_ms_list = []
    for i in range(markers_single.shape[0]):
        print(i)
        print(pat_fov_list[i])
        channel_num = np.int(pat_fov_list[i].split("_40X_")[1].split(".tiff")[0])
        ms_list.append(markers_single[channel_num-1])

    markers_single = np.copy(np.array(ms_list))
    ###

    # use this updated markers_single name order going forward
    for i in range(markers_single.shape[0]):

        #color_vec_patid.append(colours_58[clust_patid_list_1[i]]) 
        clust_ms_list.append(markers_single[i])
        cluster_ms_list.append('Channel '+ markers_single[i]) 
    '''
    
    ##added on 9th feb 2022
    ## for codex sm for tonsils
    
    ## need to update the markers_single array based on the order the files are read in 
    ms_list=[]
    cluster_ms_list = []
    for i in range(markers_single.shape[0]):
        print(i)
        print(pat_fov_list[i])
        #channel_num = np.int(pat_fov_list[i].split("_40X_")[1].split(".tiff")[0])
        channel_name = pat_fov_list[i].split('.tif')[0].split('_')[3]
        channel_num = np.int(np.array(np.where(channel_name==markers_single)).flatten())
        ms_list.append(markers_single[channel_num])

    markers_single = np.copy(np.array(ms_list))
    ###

    # use this updated markers_single name order going forward
    for i in range(markers_single.shape[0]):

        #color_vec_patid.append(colours_58[clust_patid_list_1[i]]) 
        clust_ms_list.append(markers_single[i])
        cluster_ms_list.append('Channel '+ markers_single[i]) 
    

elif (stack_montage_flag == False): 
    ###############
    ###############
    #1st Feb 2022
    ###############
    #uncomment for tcycif/vectra
    ###############
    

    ## 28th Jan 2022
    # to handle all markers in t-CyCIF

    mc = []
    for m in range(len(LABELS_MARKERS)):
        in_mc = np.int(np.array(np.where(LABELS_MARKERS[m] == np.array(markers_single))).flatten())
        mc.append(in_mc)
    wc = [150] * len(LABELS_MARKERS)      
    wc[0] = 300 #was 50 pre codex 11th feb 2022
    wc[6] = 100
    #wc[1]=wc[2]=wc[3]=wc[4]= 750 #added for codex 11th feb 2022
    