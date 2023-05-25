
def Fuck(fn, st, store):
    for check in fn:
        if check in ['\\', '/', ':', '?', '*', '"', '<', '>', '|']:
            fn = fn.replace(check, "\u2022")
            st.append(", ".join(check))
    store.append(', '.join(st))
    return fn, st, store