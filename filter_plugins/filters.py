def merge( hash_a, hash_b ):
    return dict(hash_a.items() + hash_b.items());

class FilterModule( object ):
    def filters( self ):
        return {'merge': merge}
