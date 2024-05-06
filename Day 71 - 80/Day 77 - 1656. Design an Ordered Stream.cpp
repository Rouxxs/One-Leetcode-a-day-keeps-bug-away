class OrderedStream {
public:
    int ptr;
    vector<string> stream;
    OrderedStream(int n) {
        ptr = 0;
        stream.resize(n);
    }
    
    vector<string> insert(int idKey, string value) {
        stream[idKey - 1] = value;
        vector<string> out;
        while (ptr < stream.size() && stream[ptr] != "") {
            out.push_back(stream[ptr]);
            ptr++;
        }
        return out;
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */