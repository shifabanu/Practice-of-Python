// This is a snapshot of a C program. This code has a few critical security
// Read through the code and then point out the possible security bugs.
// You have 6 minutes to complete.

int ProcessRequest(char *pUsername, char *pPassword, int reqType, int req)
{
    char msgheader[32];
    int rc, rawvalue, response;
    
    sprintf(msgheader, "%s: req by %s/%s reqtype: %u req: %u: ",
        __FUNCTION__, pUsername, pPassword, reqType, req);
    
    rc = RequestAuthorize(pUserName, pPassword, req);
    if (rc == 0)
    {
        rc = LowerLayerProcessRequest(reqType, req, &rawvalue);
        if (rc == 0) 
        {
            short mask, shift, valueshift;            
            shift = ((reqType - 1) << 2);
            mask = (0xF << shift);
            valueshift = ((rawvalue & mask) >> shift);
            if (0xC & valueshift) 
            {
                debug_print("%s: ERROR: unexpected bit value: 0x%hX\n", 
                    msgheader, valueshift,);
            }
            valueshift &= 0x3;
            response = (1 << valueshift);
        }
    }
    return response;
} // ProcessIntRequest
