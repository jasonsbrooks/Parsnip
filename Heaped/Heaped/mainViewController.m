//
//  mainViewController.m
//  Heaped
//
//  Created by Michael Zhao on 4/2/14.
//  Copyright (c) 2014 Michael Zhao. All rights reserved.
//

#import "mainViewController.h"
#import "HeapBeaconVC.h"
#import "ESTBeaconManager.h"
#import "ESTBeaconRegion.h"

@interface mainViewController () <ESTBeaconManagerDelegate>
@property ESTBeaconManager *beaconManager;
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
	// Do any additional setup after loading the view.
    
    
    self.beaconManager = [[ESTBeaconManager alloc] init];
    self.beaconManager.delegate = self;
    self.beaconManager.avoidUnknownStateBeacons = YES;
    
    ESTBeaconRegion *region = [[ESTBeaconRegion alloc] initWithProximityUUID:ESTIMOTE_PROXIMITY_UUID identifier:@"EstimoteSampleRegion"];
    
    [self.beaconManager startRangingBeaconsInRegion:region];
    
    [self setupView];
}

-(void)setupView
{
    /////////////////////////////////////////////////////////////
    // setup background image
    
    CGRect          screenRect          = [[UIScreen mainScreen] bounds];
    CGFloat         screenHeight        = screenRect.size.height;
    UIImageView    *backgroundImage;
    
    if (screenHeight > 480)
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"animal_personality.jpg"]];
    else
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"backgroundSmall"]];
    
    [self.view addSubview:backgroundImage];

}

-(void)beaconManager:(ESTBeaconManager *)manager
     didRangeBeacons:(NSArray *)beacons
            inRegion:(ESTBeaconRegion *)region
{
    ESTBeacon *beacon0;
    ESTBeacon *beacon1;

    // Detected a beacon
    if([beacons count] > 0)
    {
        // Show its distance in distance0.
        beacon0 = [beacons objectAtIndex:0];
        self.distance0.text = [beacon0.distance stringValue];

//        // If more than 1 beacon, show its distance as well.
//        if([beacons count] > 1) {
//            beacon1 = [beacons objectAtIndex:1];
//            self.distance1.text = [beacon1.distance stringValue];
//        }

        
        NSLog(@"%@", [beacon0.distance stringValue]);
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
