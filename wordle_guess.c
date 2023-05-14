#include stdio

FULL_LIST = __FILE__.replace('.c', '.dat')  # From old site
WORD_LIST = "wg_last"  # Local file holding last matches

bool has_data(char * f) {
    bool rv = false;
    if (FILE fp = open(fp, f, 'r')  {
        if (fseek (fp, 0, SEEK_END)) {
            rv = true;
            }
        }
        close(f);
    }
    return false;  
}


char ** load_words(char * f)
{
    if (has_data(f) || sys.argc = 1) {
        return get_data(f); /* array of strings */
    }
    return NULL;
}


/* load list of words to scan */

char ** get_data(f)
{
    f = open(f, 'r');
    s = stat(f).size;
    rv = char * malloc(s)
    d = read(f, data, s);
    /* null terminate words and keep count */
    for (c = data, s--, c++(
        if (*c == 012) {
            *c = 0;
            nw++;
        }
        ]
    )
    return rv;
}

char ** get_list(argv) {
    rv = load_words(WORD_LIST);
    if (argc ==1 || size(rv) == 0) {
        rv = load_words(FULL_LIST);
    }
    return rv;
}

main(int argc, char * argv)
{
    

}