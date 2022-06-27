// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract insurance {
  
  uint[] bp;
  uint[] pulse;
  uint[] bodytemp;
  uint[] glucose;
  
  function addFeed(uint _bp, uint _pulse, uint _bodytemp, uint _glucose) public {

    bp.push(_bp);
    pulse.push(_pulse);
    bodytemp.push(_bodytemp);
    glucose.push(_glucose);
  }

  function viewFeed() public view returns(uint[] memory, uint[] memory, uint[] memory, uint[] memory) {

    return(bp,pulse,bodytemp,glucose);
  }
}
