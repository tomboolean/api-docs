using System;
using System.Threading.Tasks;
using Bandwidth.Standard;
using Bandwidth.Standard.Exceptions;
using Bandwidth.Standard.MultiFactorAuth.Models;

class Program
{
    static async Task Main(string[] args)
    {
        var username = System.Environment.GetEnvironmentVariable("BW_USERNAME");
        var password = System.Environment.GetEnvironmentVariable("BW_PASSWORD");
        var accountId = System.Environment.GetEnvironmentVariable("BW_ACCOUNT_ID");
        var applicationId = System.Environment.GetEnvironmentVariable("BW_MESSAGING_APPLICATION_ID");
        var to = System.Environment.GetEnvironmentVariable("USER_NUMBER");
        var scope = "sample";
        var code = "159193";
        var expirationTimeInMinutes = 3;

        var client = new BandwidthClient.Builder()
            .MultiFactorAuthBasicAuthCredentials(username, password)
            .Build();

        var request = new TwoFactorVerifyRequestSchema
        {
            ApplicationId = applicationId,
            To = to,
            Scope = scope,
            Code = code,
            ExpirationTimeInMinutes = expirationTimeInMinutes
        };

        try
        {
            var response = await client.MultiFactorAuth.MFAController.CreateVerifyTwoFactorAsync(accountId, request);
            Console.WriteLine(response.Data);
        }
        catch (ApiException e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
