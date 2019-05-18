var Migrations = artifacts.require("./Migrations.sol");
var Bhoomi  = artifacts.require("./Bhoomi.sol");
module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(Bhoomi);
};
