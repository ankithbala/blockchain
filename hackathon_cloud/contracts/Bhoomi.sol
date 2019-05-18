pragma solidity ^0.4.18;

contract Bhoomi{
    //properties of the Owner or Details
    struct Owner{
      bytes32 name;
      uint aadharNo;
      bytes32 panNo;
      uint publicKey;

    }
    //putting the restrictions on the landNo
    function setRestriction(uint _landNo, uint[] res) public {

        for(uint i=0;i < res.length;i++){
            land st;
            st.val = res[i];
            restrict[_landNo].push(st);
        }
    }
    function getRestriction(uint _landNo,uint i) public returns(uint){
        return restrict[_landNo][i].val;
    }
    bytes32 a;

    //set new Owner which will be deprecated in the near future
    //@TODO:inefficient currently cause storing land and users details can be seperated
    function setOwner(uint _landNo,bytes32 _name,uint _aadharNo,bytes32 _panNo,uint publicKey) public returns (bytes32){
      userDetails[_landNo].name = _name;
      userDetails[_landNo].aadharNo = _aadharNo;
      userDetails[_landNo].panNo = _panNo;
      userDetails[_landNo].publicKey = publicKey;
      /* a = sha256(publicKey,privateKey,101010);
      return sha256(a,publicKey); */
    }

    //mapping of userdetails
    mapping(uint => Owner) userDetails;
    Owner t = userDetails[1];

    //land structure for the restriction
    struct land{
      uint val;
    }

    //land elements landNo => restrictions
    mapping(uint => land[])  restrict;
    land struct1;
    //initializing for testing
    //the following code has to be commented
    function  Bhoomi() public {
      t.name = "abcd";
      t.aadharNo = 1;
      t.panNo = "abcd";
      struct1.val = 0;
      restrict[0].push(struct1);
      restrict[0].push(struct1);
    }
    //structure containing the details or conflicts of an account

    function validateLandRecord(uint landNo) public returns (uint){
      for(uint i = 0;i < restrict[landNo].length;i++){
        if(restrict[landNo][i].val == 1){
          return (i+1);
        }
      }
      return 0;
    }


    //modifier to check the vaildity of the landNo

    //retreiving the owner Details of the land
    function getOwner(uint landNo) public constant returns (bytes32,uint,bytes32,uint){
      Owner  owner =  userDetails[landNo];

      return (owner.name, owner.aadharNo, owner.panNo, owner.publicKey);
      /* return ("ancd",123,"sada"); */
    }

    //a person wants to sell his land includes validation with RSA
    function sellLand(uint _landNo,uint _sellerAadharNo,uint _buyerAadharNo,bytes32 buyersName,bytes32 buyersPan,uint buyersPublicKey,uint[] msg,uint[] cipherText,uint n,uint size) public  returns(uint){
           var(, sellerAadharNo, , d)= getOwner(_landNo);

           //checking the Owner of the land
           if(sellerAadharNo != _sellerAadharNo){
            return 1;
          }
          if(decrypt(msg, cipherText, d, n, size) != true){
            return 1;
          }
          /*0 -> success
            1 ->conflicts
            */
        if(validateLandRecord(_landNo) != 0){
              return(2);
          }
        else{
          userDetails[_landNo].name = buyersName ;
          userDetails[_landNo].aadharNo = _buyerAadharNo;
          userDetails[_landNo].panNo = buyersPan;
          userDetails[_landNo].publicKey = buyersPublicKey;
          return 0;
        }
      }
      function simplifyPower(uint val,uint pk,uint n) public constant returns (uint){
        if(pk == 1){
          return val;
        }

        for(uint j = 1;j<(n);j++){
          if((val ** j ) >= n){
            uint pw = uint(pk/j);
            uint rem = pk%j;
            return ((simplifyPower((val ** j) % n,pw,n) * ((val ** rem) % n)) % n);

          }
          else{
            continue;
          }
        }
      }
      function decrypt(uint[] msg,uint[] cipherText,uint _publicKey,uint n,uint size) public  constant returns (bool){
          for(uint i =0;i<size;i++){
            if(simplifyPower(cipherText[i], _publicKey, n) != msg[i]){
              return false;
            }
          }
        return true;
      }
}
