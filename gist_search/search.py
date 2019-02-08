from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return None
    user_gists = get_gists(username)
    result = []
    
    for gist in user_gists:
        if description and description not in gist["description"]:
            continue
        if file_name:
            match = False
            for fname in gist["files"]:
                if file_name.lower() in fname.lower():
                    match = True
                    break
                if not match:
                    continue
        result.append(gist)
    return result
        
                
            
# search_gists(username = "santiagobasulto", description="Pickle", file_name = "timezone")
search_gists('santiagobasulto', file_name='timezone')
#     '''
#     python main.py -u santiagobasulto -d time
#     '''