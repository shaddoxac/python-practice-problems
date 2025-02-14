# This problem was asked by Snapchat.

# Given a string of digits, generate all possible valid IP address combinations.

# IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
# Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

# For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].

from typing import List

def gen_possible_ip_addresses(int_str: str) -> List[str]:
    ret = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    # this is a little ugly but it works 😊
                    if i+1+j+1+k+1+l+1 == len(int_str):
                        str = f"{int_str[0:i+1]}.{int_str[i+1:i+1+j+1]}.{int_str[i+1+j+1:i+1+j+1+k+1]}.{int_str[i+1+j+1+k+1:i+1+j+1+k+1+l+1]}"
                        if is_valid_ip_string(str):
                            ret.append(str)
    return ret

def is_valid_ip_string(ip_str: str) -> bool:
    if ip_str.count(".") != 3:
        return False
    for ip_section in ip_str.split("."):
        if ip_section[0] == "0" and len(ip_section) > 1:
            return False
        try:
            int(ip_section)
        except ValueError:
            return False
        if int(ip_section) < 0 or int(ip_section) > 255:
            return False
    return True

assert(is_valid_ip_string("254.254.0.123"))
assert(gen_possible_ip_addresses("2542540123") == ['254.25.40.123', '254.254.0.123'])