//
//  mainViewController.m
//  Heaped
//
//  Created by Michael Zhao on 4/2/14.
//  Copyright (c) 2014 Michael Zhao. All rights reserved.
//

#import "mainViewController.h"
#import "ESTBeaconManager.h"
#import "ESTBeaconRegion.h"

@interface mainViewController () <ESTBeaconManagerDelegate>
@property ESTBeaconManager *beaconManager;
@property ESTBeaconRegion *region;
@property ESTBeacon *beacon0;
@property ESTBeacon *beacon1;
@property ESTBeacon *beacon2;
@end

@implementation mainViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    // Beacon Manager discovers beacons.
    self.beaconManager = [[ESTBeaconManager alloc] init];
    self.beaconManager.delegate = self;
    self.beaconManager.avoidUnknownStateBeacons = YES;
    
    // Set the region (could be used to identify a store).
    self.region = [[ESTBeaconRegion alloc] initWithProximityUUID:ESTIMOTE_PROXIMITY_UUID identifier:@"EstimoteSampleRegion"];
    
    // Search for beacons within region.
//    [self.beaconManager startRangingBeaconsInRegion:self.region];
    
//    [self setupView];
}

// Set up background view for demo (not needed for our purposes.
-(void)setupView
{
    /////////////////////////////////////////////////////////////
    // setup background image
    
    CGRect          screenRect          = [[UIScreen mainScreen] bounds];
    CGFloat         screenHeight        = screenRect.size.height;
    UIImageView    *backgroundImage;
    
    if (screenHeight > 480)
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"backgroundSmall"]];
    else
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"backgroundSmall"]];
    
    [self.view addSubview:backgroundImage];

}

-(void)beaconManager:(ESTBeaconManager *)manager
     didRangeBeacons:(NSArray *)beacons
            inRegion:(ESTBeaconRegion *)region
{
    // Detected a beacon
    if([beacons count] > 0)
    {
        // Show its distance in distance0.
        self.beacon0 = [beacons objectAtIndex:0];
        self.distance0.text = [self.beacon0.distance stringValue];
        self.beaconID0.text = [self.beacon0.proximityUUID UUIDString];
        
        NSLog(@"Beacon0 Unique: %@", [self.beacon0.proximityUUID UUIDString]);
        NSLog(@"Beacon0 distance: %@", [self.beacon0.distance stringValue]);

        // If more than 1 beacon, show its distance as well.
        if([beacons count] > 1) {
            self.beacon1 = [beacons objectAtIndex:1];
            self.distance1.text = [self.beacon1.distance stringValue];
            self.beaconID1.text = [self.beacon1.proximityUUID UUIDString];
            
            if ([beacons count] > 2) {
                self.beacon2 = [beacons objectAtIndex:2];
                self.distance2.text = [self.beacon2.distance stringValue];
                self.beaconID2.text = [self.beacon2.proximityUUID UUIDString];
            }
            else
                NSLog(@"Couldn't find beacon 2.");

        }
        else
            NSLog(@"Couldn't find beacon 1.");
        
    }
    else
        NSLog(@"Couldn't find beacon 0.");
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)startData:(id)sender {
    [self.beaconManager startRangingBeaconsInRegion:self.region];
}

- (IBAction)stopData:(id)sender {
    [self.beacon0 disconnectBeacon];
    [self.beacon1 disconnectBeacon];
    [self.beacon2 disconnectBeacon];
    
//    Issue POST request here.
}
@end
