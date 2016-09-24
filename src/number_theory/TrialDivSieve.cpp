/*
   Copyright (c) 2009-2016, Jack Poulson
   All rights reserved.

   This file is part of Elemental and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
*/
#include <El.hpp>

namespace {

// Dynamic sieve for trial division
El::DynamicSieve<unsigned long long,unsigned> trialDivSieve;

}

namespace El {

DynamicSieve<unsigned long long,unsigned>& TrialDivisionSieve()
{ return ::trialDivSieve; }

} // namespace El
